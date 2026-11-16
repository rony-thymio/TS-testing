"""Tiny builder for Scratch 3 projects using the Thymio extension (used by make_scratch_activities.py).

Blocks are written as nested Python calls; build() returns the sprite's "blocks" dictionary and
variables in the Scratch 3 project.json format. The final .sb3 is produced by Scratch itself
(tools/build_sb3.py loads the JSON into Mobsya's Scratch and saves it), so it is always valid.
"""
import itertools

_ids = itertools.count(1)


def _id():
    return f"b{next(_ids)}"


class Block:
    def __init__(self, opcode, inputs=None, fields=None, shadow=False, mutation=None):
        self.id = _id()
        inputs, fields = dict(inputs or {}), dict(fields or {})
        # Thymio extension menus are plain fields on the block (as in Scratch's own toolbox XML)
        for k, v in list(inputs.items()):
            if isinstance(v, tuple) and v[0] == 'field':
                fields[k] = [v[1], None]
                del inputs[k]
        self.opcode, self.inputs, self.fields = opcode, inputs, fields
        self.shadow, self.mutation = shadow, mutation


# --- input helpers --------------------------------------------------------------------------
def num(v):
    return ('num', v)


def txt(v):
    return ('txt', v)


def menu(opcode, field, value):
    return ('menu', Block(opcode, fields={field: [value, None]}, shadow=True))


def field(value):
    return ('field', value)


def sub(*stack):
    return ('sub', list(stack))


# --- Thymio blocks ---------------------------------------------------------------------------
SENSOR = {'left': 0, 'front-left': 1, 'centre': 2, 'front-right': 3, 'right': 4, 'back-left': 5, 'back-right': 6}


def motor(which, speed):            # which: left | right | all
    return Block('thymio_setMotor', {'M': field(which), 'N': _v(speed)})


def stop_motors():
    return Block('thymio_stopMotors')


def leds(where, r, g, b):           # where: all | top | bottom | bottom-left | bottom-right
    return Block('thymio_leds', {'L': field(where), 'R': _v(r), 'G': _v(g), 'B': _v(b)})


def clear_leds():
    return Block('thymio_clearLeds')


def prox(sensor):                   # reporter: horizontal proximity sensor value
    return Block('thymio_proximity', {'N': field(str(SENSOR[sensor]))})


def ground(n):
    return Block('thymio_ground', {'N': field(str(n))})


def when_button(button):            # center | front | back | left | right
    return Block('thymio_whenButton', {'B': field(button)})


def note(hz, seconds):
    return Block('thymio_soundFreq', {'N': _v(hz), 'S': _v(seconds)})


def system_sound(n):
    return Block('thymio_soundSystem', {'S': field(str(n))})


def move(mm):
    return Block('thymio_move', {'N': _v(mm)})


def turn(deg):
    return Block('thymio_turn', {'N': _v(deg)})


def arc(radius, angle):
    return Block('thymio_arc', {'R': _v(radius), 'A': _v(angle)})


def mic():
    return Block('thymio_micIntensity')


def leds_temperature(r, b):
    return Block('thymio_ledsTemperature', {'A': _v(r), 'B': _v(b)})


def leds_ground(a, b):
    return Block('thymio_ledsProxV', {'A': _v(a), 'B': _v(b)})


# --- Scratch blocks ------------------------------------------------------------------------------
def when_flag():
    return Block('event_whenflagclicked')


def when_key(key):
    return Block('event_whenkeypressed', fields={'KEY_OPTION': [key, None]})


def forever(*stack):
    return Block('control_forever', {'SUBSTACK': sub(*stack)})


def repeat(times, *stack):
    return Block('control_repeat', {'TIMES': _v(times), 'SUBSTACK': sub(*stack)})


def repeat_until(cond, *stack):
    return Block('control_repeat_until', {'CONDITION': ('bool', cond), 'SUBSTACK': sub(*stack)})


def if_(cond, *stack):
    return Block('control_if', {'CONDITION': ('bool', cond), 'SUBSTACK': sub(*stack)})


def if_else(cond, then, otherwise):
    return Block('control_if_else', {'CONDITION': ('bool', cond), 'SUBSTACK': sub(*then), 'SUBSTACK2': sub(*otherwise)})


def wait(seconds):
    return Block('control_wait', {'DURATION': ('pos', seconds)})


def wait_until(cond):
    return Block('control_wait_until', {'CONDITION': ('bool', cond)})


def gt(a, b):
    return Block('operator_gt', {'OPERAND1': _t(a), 'OPERAND2': _t(b)})


def lt(a, b):
    return Block('operator_lt', {'OPERAND1': _t(a), 'OPERAND2': _t(b)})


def eq(a, b):
    return Block('operator_equals', {'OPERAND1': _t(a), 'OPERAND2': _t(b)})


def or_(a, b):
    return Block('operator_or', {'OPERAND1': ('bool', a), 'OPERAND2': ('bool', b)})


def and_(a, b):
    return Block('operator_and', {'OPERAND1': ('bool', a), 'OPERAND2': ('bool', b)})


def sub_(a, b):
    return Block('operator_subtract', {'NUM1': _v(a), 'NUM2': _v(b)})


def add_(a, b):
    return Block('operator_add', {'NUM1': _v(a), 'NUM2': _v(b)})


def div_(a, b):
    return Block('operator_divide', {'NUM1': _v(a), 'NUM2': _v(b)})


def join(a, b):
    return Block('operator_join', {'STRING1': _t(a), 'STRING2': _t(b)})


def key_pressed(key):
    return Block('sensing_keypressed', {'KEY_OPTION': menu('sensing_keyoptions', 'KEY_OPTION', key)})


def say(msg):
    return Block('looks_say', {'MESSAGE': _t(msg)})


def var(name):
    return Block('data_variable', fields={'VARIABLE': [name, 'var-' + name]})


def set_var(name, value):
    return Block('data_setvariableto', {'VALUE': _t(value)}, {'VARIABLE': [name, 'var-' + name]})


def change_var(name, by):
    return Block('data_changevariableby', {'VALUE': _v(by)}, {'VARIABLE': [name, 'var-' + name]})


def define(name, *stack):
    """custom block without inputs ("My Blocks")"""
    proto = Block('procedures_prototype', shadow=True,
                  mutation={'tagName': 'mutation', 'children': [], 'proccode': name, 'argumentids': '[]',
                            'argumentnames': '[]', 'argumentdefaults': '[]', 'warp': 'false'})
    return [Block('procedures_definition', {'custom_block': ('proto', proto)})] + list(stack)


def call(name):
    return Block('procedures_call', mutation={'tagName': 'mutation', 'children': [], 'proccode': name,
                                              'argumentids': '[]', 'warp': 'false'})


def _v(x):
    return x if isinstance(x, (Block, tuple)) else num(x)


def _t(x):
    if isinstance(x, (Block, tuple)):
        return x
    return num(x) if isinstance(x, (int, float)) else txt(x)


# --- serialisation -------------------------------------------------------------------------------
def build(scripts):
    """scripts: list of lists of Blocks (each list = one script, first block a hat or definition)."""
    blocks, variables = {}, {}

    def put(b, parent):
        d = {'opcode': b.opcode, 'next': None, 'parent': parent, 'inputs': {}, 'fields': b.fields,
             'shadow': b.shadow, 'topLevel': False}
        if b.mutation:
            d['mutation'] = b.mutation
        for f in b.fields.values():
            if isinstance(f, list) and len(f) == 2 and isinstance(f[1], str) and f[1].startswith('var-'):
                variables[f[1]] = [f[0], 0]
        blocks[b.id] = d
        for name, val in b.inputs.items():
            d['inputs'][name] = encode(val, b.id)
        return d

    def encode(val, parent):
        if isinstance(val, Block):
            put(val, parent)
            return [3, val.id, [4, '0']]
        kind, v = val
        if kind == 'num':
            return [1, [4, str(v)]]
        if kind == 'pos':
            return [1, [5, str(v)]] if not isinstance(v, Block) else encode(v, parent)
        if kind == 'txt':
            return [1, [10, str(v)]]
        if kind == 'menu':
            put(v, parent)
            return [1, v.id]
        if kind == 'proto':
            put(v, parent)
            return [1, v.id]
        if kind == 'bool':
            put(v, parent)
            return [2, v.id]
        if kind == 'sub':
            first = chain(v, parent)
            return [2, first]
        raise ValueError(kind)

    def chain(stack, parent):
        prev = None
        for b in stack:
            d = put(b, prev.id if prev else parent)
            if prev:
                blocks[prev.id]['next'] = b.id
            prev = b
        return stack[0].id if stack else None

    y = 40
    for script in scripts:
        chain(script, None)
        top = blocks[script[0].id]
        top.update({'topLevel': True, 'x': 40, 'y': y})
        y += 120 + 48 * _count(script)
    return blocks, variables


def _count(stack):
    n = 0
    for b in stack:
        n += 1
        for val in b.inputs.values():
            if isinstance(val, tuple) and val[0] == 'sub':
                n += _count(val[1])
    return n
