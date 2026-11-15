// Minimal FlexBuffers reader/writer for the values exchanged with the Thymio Device Manager
// (variables, events, constants). Spec: https://flatbuffers.dev/flexbuffers/
// Reads: null, bool, int, uint, float, strings, keys, untyped and typed vectors, maps (as objects).
// Writes: an integer or an array of integers (all Aseba values are 16-bit integers).
(function (root) {
  'use strict';
  const T = { NULL: 0, INT: 1, UINT: 2, FLOAT: 3, KEY: 4, STRING: 5, IND_INT: 6, IND_UINT: 7, IND_FLOAT: 8,
    MAP: 9, VECTOR: 10, VEC_INT: 11, VEC_UINT: 12, VEC_FLOAT: 13, VEC_KEY: 14, VEC_STRING_DEPRECATED: 15,
    VEC_INT2: 16, VEC_UINT2: 17, VEC_FLOAT2: 18, VEC_INT3: 19, VEC_UINT3: 20, VEC_FLOAT3: 21,
    VEC_INT4: 22, VEC_UINT4: 23, VEC_FLOAT4: 24, BLOB: 25, BOOL: 26, VEC_BOOL: 36 };

  function decode(bytes) {
    const buf = bytes instanceof Uint8Array ? bytes : new Uint8Array(bytes);
    if (buf.length < 3) return null;
    const dv = new DataView(buf.buffer, buf.byteOffset, buf.byteLength);
    const readUInt = (o, w) => w === 1 ? dv.getUint8(o) : w === 2 ? dv.getUint16(o, true) : w === 4 ? dv.getUint32(o, true) : Number(dv.getBigUint64(o, true));
    const readInt = (o, w) => w === 1 ? dv.getInt8(o) : w === 2 ? dv.getInt16(o, true) : w === 4 ? dv.getInt32(o, true) : Number(dv.getBigInt64(o, true));
    const readFloat = (o, w) => w === 4 ? dv.getFloat32(o, true) : w === 8 ? dv.getFloat64(o, true) : readInt(o, w);
    const indirect = (o, w) => o - readUInt(o, w);
    const cstr = (o) => { let e = o; while (e < buf.length && buf[e] !== 0) e++; return new TextDecoder().decode(buf.subarray(o, e)); };

    function value(offset, parentWidth, packedType) {
      const type = packedType >> 2;
      const width = 1 << (packedType & 3);
      switch (type) {
        case T.NULL: return null;
        case T.INT: return readInt(offset, parentWidth);
        case T.UINT: return readUInt(offset, parentWidth);
        case T.FLOAT: return readFloat(offset, parentWidth);
        case T.BOOL: return readUInt(offset, parentWidth) !== 0;
        case T.IND_INT: return readInt(indirect(offset, parentWidth), width);
        case T.IND_UINT: return readUInt(indirect(offset, parentWidth), width);
        case T.IND_FLOAT: return readFloat(indirect(offset, parentWidth), width);
        case T.KEY: return cstr(indirect(offset, parentWidth));
        case T.STRING: {
          const p = indirect(offset, parentWidth); const n = readUInt(p - width, width);
          return new TextDecoder().decode(buf.subarray(p, p + n));
        }
        case T.VECTOR: case T.MAP: {
          const p = indirect(offset, parentWidth); const n = readUInt(p - width, width);
          const items = [];
          for (let i = 0; i < n; i++) items.push(value(p + i * width, width, buf[p + n * width + i]));
          if (type === T.VECTOR) return items;
          // map: keys vector offset and width are stored just before the size
          const keysP = indirect(p - 3 * width, width); const keysW = readUInt(p - 2 * width, width);
          const obj = {};
          for (let i = 0; i < n; i++) obj[cstr(indirect(keysP + i * keysW, keysW))] = items[i];
          return obj;
        }
        case T.VEC_INT: case T.VEC_UINT: case T.VEC_FLOAT: case T.VEC_BOOL: case T.VEC_KEY: {
          const p = indirect(offset, parentWidth); const n = readUInt(p - width, width);
          const out = [];
          for (let i = 0; i < n; i++) {
            const o = p + i * width;
            out.push(type === T.VEC_INT ? readInt(o, width) : type === T.VEC_FLOAT ? readFloat(o, width)
              : type === T.VEC_KEY ? cstr(indirect(o, width)) : type === T.VEC_BOOL ? readUInt(o, width) !== 0 : readUInt(o, width));
          }
          return out;
        }
        default:
          if (type >= T.VEC_INT2 && type <= T.VEC_FLOAT4) {
            const n = 2 + Math.floor((type - T.VEC_INT2) / 3); const k = (type - T.VEC_INT2) % 3;
            const p = indirect(offset, parentWidth); const out = [];
            for (let i = 0; i < n; i++) out.push(k === 0 ? readInt(p + i * width, width) : k === 1 ? readUInt(p + i * width, width) : readFloat(p + i * width, width));
            return out;
          }
          return null; // blobs and others are not used by the device manager
      }
    }
    const rootWidth = buf[buf.length - 1];
    const rootType = buf[buf.length - 2];
    return value(buf.length - 2 - rootWidth, rootWidth, rootType);
  }

  // Encodes an integer, or an array of integers as a typed int vector, with 16- or 32-bit width.
  function encode(v) {
    if (v === null || v === undefined) return new Uint8Array([0, T.NULL << 2, 1]);
    const fits16 = (n) => n >= -32768 && n <= 32767;
    if (Array.isArray(v)) {
      const ints = v.map((x) => Math.trunc(Number(x)) || 0);
      const w = ints.every(fits16) && ints.length <= 32767 ? 2 : 4;
      const bytes = [];
      const push = (n) => { for (let i = 0; i < w; i++) bytes.push((n >> (8 * i)) & 0xff); };
      push(ints.length);
      const start = bytes.length;
      ints.forEach(push);
      // root: offset back to the vector start, stored with the same width
      const rootAt = bytes.length;
      push(rootAt - start);
      bytes.push((T.VEC_INT << 2) | (w === 2 ? 1 : 2), w);
      return new Uint8Array(bytes);
    }
    const n = Math.trunc(Number(v)) || 0;
    const w = fits16(n) ? 2 : 4;
    const bytes = [];
    for (let i = 0; i < w; i++) bytes.push((n >> (8 * i)) & 0xff);
    bytes.push((T.INT << 2) | (w === 2 ? 1 : 2), w);
    return new Uint8Array(bytes);
  }

  root.FlexBuffers = { decode, encode };
})(typeof window !== 'undefined' ? window : globalThis);
