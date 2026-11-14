/* Developer-only stand-in for the DNS-SD (Bonjour) library on Linux machines that have neither
 * Avahi's compatibility layer nor mDNSResponder installed. Every call reports that the zeroconf
 * service is not running, which also lets us test how the device manager behaves on networks
 * where zeroconf is blocked (common in schools). Never used for release builds. */
#include <stddef.h>
#include <stdint.h>
#include <string.h>
#include "dns_sd.h"

#define NOT_RUNNING kDNSServiceErr_ServiceNotRunning

DNSServiceErrorType DNSSD_API DNSServiceCreateConnection(DNSServiceRef* r) { if(r) *r = NULL; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceBrowse(DNSServiceRef* r, DNSServiceFlags f, uint32_t i, const char* t,
    const char* d, DNSServiceBrowseReply cb, void* c) { (void)f;(void)i;(void)t;(void)d;(void)cb;(void)c; if(r) *r = NULL; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceResolve(DNSServiceRef* r, DNSServiceFlags f, uint32_t i, const char* n,
    const char* t, const char* d, DNSServiceResolveReply cb, void* c) { (void)f;(void)i;(void)n;(void)t;(void)d;(void)cb;(void)c; if(r) *r = NULL; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceGetAddrInfo(DNSServiceRef* r, DNSServiceFlags f, uint32_t i,
    DNSServiceProtocol p, const char* h, DNSServiceGetAddrInfoReply cb, void* c) { (void)f;(void)i;(void)p;(void)h;(void)cb;(void)c; if(r) *r = NULL; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceRegister(DNSServiceRef* r, DNSServiceFlags f, uint32_t i, const char* n,
    const char* t, const char* d, const char* h, uint16_t port, uint16_t len, const void* txt,
    DNSServiceRegisterReply cb, void* c) { (void)f;(void)i;(void)n;(void)t;(void)d;(void)h;(void)port;(void)len;(void)txt;(void)cb;(void)c; if(r) *r = NULL; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceUpdateRecord(DNSServiceRef r, DNSRecordRef rr, DNSServiceFlags f,
    uint16_t len, const void* data, uint32_t ttl) { (void)r;(void)rr;(void)f;(void)len;(void)data;(void)ttl; return NOT_RUNNING; }
DNSServiceErrorType DNSSD_API DNSServiceProcessResult(DNSServiceRef r) { (void)r; return NOT_RUNNING; }
void DNSSD_API DNSServiceRefDeallocate(DNSServiceRef r) { (void)r; }
int DNSSD_API DNSServiceRefSockFD(DNSServiceRef r) { (void)r; return -1; }

/* TXT record helpers: minimal working implementation (they do not need the daemon). */
typedef struct { uint8_t* buf; uint16_t len; uint16_t cap; } txt_t;
void DNSSD_API TXTRecordCreate(TXTRecordRef* t, uint16_t cap, void* buf) {
    txt_t* x = (txt_t*)t; x->buf = (uint8_t*)buf; x->len = 0; x->cap = buf ? cap : 0; }
void DNSSD_API TXTRecordDeallocate(TXTRecordRef* t) { (void)t; }
DNSServiceErrorType DNSSD_API TXTRecordSetValue(TXTRecordRef* t, const char* key, uint8_t vlen, const void* v) {
    txt_t* x = (txt_t*)t; size_t klen = strlen(key); size_t n = klen + (v ? 1 + vlen : 0);
    if(n > 255 || x->len + 1 + n > x->cap) return kDNSServiceErr_NoMemory;
    x->buf[x->len++] = (uint8_t)n; memcpy(x->buf + x->len, key, klen); x->len += (uint16_t)klen;
    if(v) { x->buf[x->len++] = '='; memcpy(x->buf + x->len, v, vlen); x->len += vlen; }
    return kDNSServiceErr_NoError; }
uint16_t DNSSD_API TXTRecordGetLength(const TXTRecordRef* t) { return ((const txt_t*)t)->len; }
const void* DNSSD_API TXTRecordGetBytesPtr(const TXTRecordRef* t) { return ((const txt_t*)t)->buf; }
uint16_t DNSSD_API TXTRecordGetCount(uint16_t len, const void* rec) {
    const uint8_t* p = (const uint8_t*)rec; uint16_t n = 0, i = 0;
    while(i < len) { i = (uint16_t)(i + 1 + p[i]); n++; } return n; }
DNSServiceErrorType DNSSD_API TXTRecordGetItemAtIndex(uint16_t len, const void* rec, uint16_t idx, uint16_t klen,
    char* key, uint8_t* vlen, const void** v) {
    const uint8_t* p = (const uint8_t*)rec; uint16_t i = 0;
    while(i < len && idx) { i = (uint16_t)(i + 1 + p[i]); idx--; }
    if(i >= len) return kDNSServiceErr_Invalid;
    { uint8_t n = p[i]; const uint8_t* s = p + i + 1; uint16_t k = 0;
      while(k < n && s[k] != '=') k++;
      if(k + 1 > klen) return kDNSServiceErr_NoMemory;
      memcpy(key, s, k); key[k] = 0;
      if(k < n) { *v = s + k + 1; *vlen = (uint8_t)(n - k - 1); } else { *v = NULL; *vlen = 0; } }
    return kDNSServiceErr_NoError; }
