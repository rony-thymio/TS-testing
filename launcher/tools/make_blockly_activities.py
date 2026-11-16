#!/usr/bin/env python3
"""Writes the Blockly activities (activities/blockly/<id>/activity.md + solution.aesl).

New activities written for Thymio Suite. Solutions are Thymio Blockly workspaces saved in the same
.aesl format as Blockly's own "Save" (the Aseba code is filled in by tools/check_blockly.py, which
opens each file in Blockly and saves the code Blockly generates).
Run from launcher/:  python3 tools/make_blockly_activities.py && python3 tools/check_blockly.py
"""
import os
from xml.sax.saxutils import escape

OWN = 'Thymio Suite activities'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'activities', 'blockly')
AGE = {1: '8+', 2: '10+', 3: '12+'}


# ---------- tiny XML builder ----------------------------------------------------------------
def B(type_, fields=None, values=None, statements=None, mutation=None):
    return dict(type=type_, fields=fields or {}, values=values or {}, statements=statements or {}, mutation=mutation)


def num(n):
    return ('num', n)


def xml_block(b, x=None, y=None, nxt=None):
    pos = f' x="{x}" y="{y}"' if x is not None else ''
    s = f'<block type="{b["type"]}"{pos}>'
    if b['mutation']:
        s += b['mutation']
    for k, v in b['fields'].items():
        s += f'<field name="{k}">{escape(str(v))}</field>'
    for k, v in b['values'].items():
        if isinstance(v, tuple) and v[0] == 'num':
            s += f'<value name="{k}"><shadow type="math_number"><field name="NUM">{v[1]}</field></shadow></value>'
        else:
            s += f'<value name="{k}">{xml_block(v)}</value>'
    for k, stack in b['statements'].items():
        s += f'<statement name="{k}">{xml_stack(stack)}</statement>'
    if nxt:
        s += f'<next>{nxt}</next>'
    return s + '</block>'


def xml_stack(stack, x=None, y=None):
    out = None
    for b in reversed(stack[1:]):
        out = xml_block(b, nxt=out)
    return xml_block(stack[0], x, y, nxt=out)


# ---------- Thymio blocks ------------------------------------------------------------------
BUTTON = {'center': 'button.center', 'forward': 'button.forward', 'backward': 'button.backward', 'left': 'button.left', 'right': 'button.right'}
PROX = {'left': 0, 'front-left': 1, 'middle': 2, 'front-right': 3, 'right': 4, 'back-left': 5, 'back-right': 6}


def on_button(button, *stack):
    return B('thymio_event_button', {'BUTTON': BUTTON[button], 'MODE': 'PRESS'}, statements={'HANDLER': list(stack)})


def on_prox(sensor, mode, *stack):          # mode PROX / NOPROX
    return B('thymio_event_prox', {'SENSOR': f'prox.horizontal[{PROX[sensor]}]', 'MODE': mode}, statements={'HANDLER': list(stack)})


def on_update(event, *stack):               # prox, buttons, temperature, acc, motor
    return B('thymio_event_update', {'EVENT': event}, statements={'HANDLER': list(stack)})


def on_timer(*stack):
    return B('thymio_event_timer', {'EVENT': 'timer0'}, statements={'HANDLER': list(stack)})


def on_sound(*stack):
    return B('thymio_event_sound', {'EVENT': 'mic'}, statements={'HANDLER': list(stack)})


def on_shock(*stack):
    return B('thymio_event_shock', statements={'HANDLER': list(stack)})


def set_timer(ms):
    return B('thymio_actuator_timer', {'VARIABLE': 'timer.period[0]'}, {'VALUE': num(ms)})


def set_mic_threshold(t):
    return B('thymio_actuator_mic', values={'VALUE': num(t)})


def drive(command, speed):                  # FORWARD BACKWARD TURNLEFT TURNRIGHT SPINCCW SPINCW
    return B('thymio_motors_start', {'COMMAND': command}, {'SPEED': num(speed)})


def stop():
    return B('thymio_motors_stop')


def motor(side, value):                     # side left / right
    return B('thymio_actuator_motor', {'VARIABLE': f'motor.{side}.target'}, {'VALUE': value if isinstance(value, dict) else num(value)})


def led(color, where='leds.top'):
    return B('thymio_led', {'LED': where, 'COLOR': color})


def led_rgb(r, g, b, where='leds.top'):
    v = lambda x: x if isinstance(x, dict) else num(x)
    return B('thymio_led_rgb', {'LED': where}, {'RED': v(r), 'GREEN': v(g), 'BLUE': v(b)})


def led_off(where='leds.top'):
    return B('thymio_led_off', {'LED': where})


def sound(n):
    return B('thymio_sound_system', {'SOUND': str(n)})


def note(freq, duration):
    v = lambda x: x if isinstance(x, dict) else num(x)
    return B('thymio_sound_note', values={'FREQ': v(freq), 'DURATION': v(duration)})


def prox_value(sensor):
    return B('thymio_sensor_prox', {'SENSOR': f'prox.horizontal[{PROX[sensor]}]'})


def temperature():
    return B('thymio_sensor_temperature', {'SENSOR': 'temperature'})


def ground_is(side, mode):                  # side 0 left / 1 right, mode BLACK / WHITE
    return B('thymio_prox_ground_check', {'SENSOR': f'prox.ground.delta[{side}]', 'MODE': mode})


def prox_is(sensor, mode):
    return B('thymio_prox_check', {'SENSOR': f'prox.horizontal[{PROX[sensor]}]', 'MODE': mode})


def compare(a, op, b):                      # op EQ NEQ LT LTE GT GTE
    v = lambda x: x if isinstance(x, dict) else num(x)
    return B('thymio_compare', {'OP': op}, {'A': v(a), 'B': v(b)})


def arith(a, op, b):                        # + - * / %
    v = lambda x: x if isinstance(x, dict) else num(x)
    return B('thymio_arithmetic', {'OP': op}, {'A': v(a), 'B': v(b)})


def logic(a, op, b):                        # AND / OR
    return B('logic_operation', {'OP': op}, {'A': a, 'B': b})


def set_var(name, value):
    return B('thymio_variable_set', {'VAR': name}, {'VALUE': value if isinstance(value, dict) else num(value)})


def get_var(name):
    return B('thymio_variable_get', {'VAR': name})


def if_(cond, then, otherwise=None):
    b = B('controls_if', values={'IF0': cond}, statements={'DO0': then})
    if otherwise:
        b['statements']['ELSE'] = otherwise
        b['mutation'] = '<mutation else="1"></mutation>'
    return b


def when(cond, *stack):
    return B('thymio_when', values={'WHEN': cond}, statements={'DO': list(stack)})


A = []
A.append(dict(id='01-colour-buttons', title='Colour buttons', level=1, needs='Nothing else needed', md='''
## The story
Thymio has five buttons and a light on its top. Let's turn it into a colour box: each button gives its own colour.

## Your goal
Each arrow button lights Thymio up in a different colour; the centre button switches the light off.

## Step by step
1. From **Events**, drag the block "when button … is pressed" and choose the forward button.
2. From **LEDs**, put a "set top LED colour" block inside it and pick a colour.
3. Do the same for the backward, left and right buttons, each with another colour.
4. Centre button: switch the top LED off.
5. Click ▶ to send the program to Thymio, then press its buttons.

## Hints
1. Each button needs its own event block: 5 blocks in total.
2. Click the colour square in the LED block to choose a colour.
3. Look at the code on the right: each event block becomes an `onevent buttons` section.

## To go further
Use the bottom LEDs too: forward lights the top, backward lights the bottom.
''', scripts=[[on_button('forward', led('#ff0000'))], [on_button('backward', led('#00ff00'))],
              [on_button('left', led('#0000ff'))], [on_button('right', led('#ffff00'))],
              [on_button('center', led_off())]]))

A.append(dict(id='02-drive-buttons', title='Drive with the buttons', level=1, needs='Some free space on a table or the floor', md='''
## The story
Thymio is a small car and its buttons are the steering wheel.

## Your goal
Drive Thymio with its buttons: forward, backward, turn left, turn right, and stop with the centre button.

## Step by step
1. "when button forward is pressed" → "start motors moving forward" at speed 200.
2. Backward button → moving backward.
3. Left button → turning left; right button → turning right.
4. Centre button → "stop motors".

## Hints
1. The "start motors" block in **Actuators** has a menu to choose the movement.
2. Speeds go up to 500. Start slowly (200) to keep control.
3. One event block per button, like in "Colour buttons".

## To go further
Add a colour for each movement, so you can see from far away what Thymio is doing.
''', scripts=[[on_button('forward', drive('FORWARD', 200))], [on_button('backward', drive('BACKWARD', 200))],
              [on_button('left', drive('TURNLEFT', 200))], [on_button('right', drive('TURNRIGHT', 200))],
              [on_button('center', stop())]]))

A.append(dict(id='03-hello-hand', title='Hello hand', level=1, needs='Nothing else needed', md='''
## The story
Thymio is polite: when you hold out your hand, it says hello with a sound and a green light.

## Your goal
When a hand comes in front of Thymio's middle sensor, it lights up green and plays a sound. When the hand goes away, the light switches off.

## Step by step
1. From **Events**, use "when front middle sensor detects an object".
2. Inside: top LED green and a system sound.
3. Add a second event: "when front middle sensor detects no object" → top LED off.
4. Send the program and wave your hand.

## Hints
1. The proximity event has two menus: which sensor, and "object" or "no object".
2. The event only fires when the situation changes, so the sound plays once per hello.
3. System sounds are in **Actuators**: try a few to find a friendly one.

## To go further
Use all five front sensors, each with its own colour, to see which one detects your hand.
''', scripts=[[on_prox('middle', 'PROX', led('#00ff00'), sound(6))], [on_prox('middle', 'NOPROX', led_off())]]))

A.append(dict(id='04-stay-on-table', title='Stay on the table', level=1, needs='A light-coloured table. Keep a hand ready the first time!', md='''
## The story
Thymio explores the table, but tables have edges… Its two ground sensors look down and can feel the void.

## Your goal
Thymio drives forward when you press the forward button, and stops by itself at the edge of the table.

## Step by step
1. Forward button → drive forward at speed 150.
2. From **Events**, use the "sensors updated" event (prox): it runs 10 times per second.
3. Inside, use "when" with the condition "left ground sensor sees black": over the void, the sensor reacts like on black.
4. Then: stop the motors and play a sound.

## Hints
1. "when … do" (in **Logic**) runs its blocks only at the moment the condition becomes true.
2. The ground sensor check is in **Sensors**: choose the left sensor and "black".
3. Test slowly, with a hand ready to catch Thymio!

## To go further
Make Thymio back up and turn instead of stopping, so it can keep exploring.
''', scripts=[[on_button('forward', drive('FORWARD', 150))],
              [on_update('prox', when(ground_is(0, 'BLACK'), stop(), sound(5)))]]))

A.append(dict(id='05-police-car', title='Police car', level=2, needs='Nothing else needed', md='''
## The story
Emergency! Thymio becomes a police car with flashing lights: red, blue, red, blue…

## Your goal
When you press the forward button, Thymio drives and its light flashes red and blue every half second, with a two-tone siren. The centre button stops everything.

## Step by step
1. Use a timer: "set timer 0 period to 500" ms, when the forward button is pressed.
2. Use a variable **flash** that switches between 0 and 1 at each timer event.
3. In the "timer 0" event: if flash is 0, red light, high note, then flash = 1; else blue light, low note, flash = 0.
4. Centre button: stop the motors, set the timer period to 0 (stopped) and switch the light off.

## Hints
1. The timer blocks are in **Events**: one to set the period, one "when timer 0 fires".
2. Variables are created in the **Variables** category.
3. "if … else" is in **Logic**; click the gear on the "if" block to add an "else".
4. Note durations are in 1/60 s: 30 means half a second.

## To go further
Make the siren faster when the car goes faster (forward button pressed again).
''', scripts=[[on_button('forward', set_var('flash', 0), set_timer(500), drive('FORWARD', 150))],
              [on_timer(if_(compare(get_var('flash'), 'EQ', 0),
                            [led('#ff0000'), note(880, 25), set_var('flash', 1)],
                            [led('#0000ff'), note(660, 25), set_var('flash', 0)]))],
              [on_button('center', stop(), set_timer(0), led_off())]]))

A.append(dict(id='06-obstacle-avoider', title='Obstacle avoider', level=2, needs='A few objects or walls', md='''
## The story
Thymio is a robot vacuum cleaner: it drives around the room and turns away from every obstacle.

## Your goal
Thymio drives forward. When it sees something in front, it turns on the spot until the way is free, then drives on.

## Step by step
1. Forward button → drive forward at speed 200.
2. "when front middle sensor detects an object" → spin on the spot (turn clockwise).
3. "when front middle sensor detects no object" → drive forward again.
4. Centre button → stop.

## Hints
1. Events fire when something changes: object appears, object disappears.
2. "spin clockwise" is one of the choices of the "start motors" block.
3. If Thymio grazes objects on the sides, add events for the front-left and front-right sensors too.

## To go further
Turn left when the obstacle is on the right and right when it is on the left, using the side sensors.
''', scripts=[[on_button('forward', drive('FORWARD', 200))],
              [on_prox('middle', 'PROX', drive('SPINCW', 200), led('#ff8000'))],
              [on_prox('middle', 'NOPROX', drive('FORWARD', 200), led('#00ff00'))],
              [on_button('center', stop(), led_off())]]))

A.append(dict(id='07-line-follower', title='Line follower', level=2, needs='A black line (about 4 cm wide) on white paper', md='''
## The story
Thymio is a train and the black line is its rail.

## Your goal
Thymio follows a black line using its two ground sensors.

## Step by step
1. Use the "sensors updated" event (prox) and an "if" block inside.
2. Both sensors on black → go straight.
3. Only the left sensor on black → turn left (left wheel slow, right wheel fast).
4. Only the right sensor on black → turn right.
5. Both on white → turn on the spot to find the line again.

## Hints
1. "if" can have several "else if" parts: click its gear to add them.
2. Combine two checks with "and" from **Logic**.
3. Set each wheel with "set motor left/right target" in **Actuators**: for example left 50, right 200.

## To go further
Speed up a little on straight parts and slow down in the bends.
''', scripts=[[on_update('prox',
                          if_(logic(ground_is(0, 'BLACK'), 'AND', ground_is(1, 'BLACK')),
                              [motor('left', 200), motor('right', 200)],
                              [if_(ground_is(0, 'BLACK'), [motor('left', 50), motor('right', 200)],
                                   [if_(ground_is(1, 'BLACK'), [motor('left', 200), motor('right', 50)],
                                        [motor('left', 150), motor('right', -150)])])]))]]))

A.append(dict(id='08-clap-to-start', title='Clap to start', level=2, needs='A fairly quiet room', md='''
## The story
Thymio obeys the sound of your hands: one clap and it goes, another clap and it stops.

## Your goal
Each clap switches Thymio between driving and stopped.

## Step by step
1. At the start (a block outside any event), set the microphone threshold to 250 and a variable **moving** to 0.
2. Use the event "when a sound is detected" (mic).
3. Inside: if moving is 0, drive forward and set moving to 1; else stop and set moving to 0.

## Hints
1. Blocks placed outside any event run once, when the program starts.
2. The threshold decides how loud the sound must be: higher means you must clap louder.
3. The motors make noise too! If Thymio stops by itself, raise the threshold.

## To go further
Two claps quickly → turn around. (Use a timer to measure the time between claps.)
''', scripts=[[set_mic_threshold(250), set_var('moving', 0)],
              [on_sound(if_(compare(get_var('moving'), 'EQ', 0),
                            [drive('FORWARD', 150), led('#00ff00'), set_var('moving', 1)],
                            [stop(), led('#ff0000'), set_var('moving', 0)]))]]))

A.append(dict(id='09-thermometer', title='Thermometer', level=2, needs='Nothing else needed (try near a window or in your hands)', md='''
## The story
Thymio has a temperature sensor inside. Let's make it show whether the room is cold, comfortable or hot.

## Your goal
Thymio's top light shows the temperature: blue below 20 °C, green between 20 and 26 °C, red above 26 °C.

## Step by step
1. Use the event "temperature updated" (it runs about once per second).
2. The temperature is given in tenths of a degree: 200 means 20.0 °C.
3. If the temperature is below 200 → blue. Else if it is above 260 → red. Else → green.

## Hints
1. The temperature value is in **Sensors**.
2. Use the comparison block from **Logic** with "<" and ">".
3. Hold Thymio in your hands for a minute: does the colour change?

## To go further
Also light the two temperature LEDs (in **LEDs**): red for heat, blue for cold.
''', scripts=[[on_update('temperature',
                          if_(compare(temperature(), 'LT', 200), [led('#0000ff')],
                              [if_(compare(temperature(), 'GT', 260), [led('#ff0000')], [led('#00ff00')])]))]]))

A.append(dict(id='10-theremin', title='Theremin', level=3, needs='Nothing else needed', md='''
## The story
The theremin is a strange musical instrument that you play without touching it: the closer your hand, the higher the note. Thymio can be one too!

## Your goal
When you bring your hand close to Thymio's front, it plays a note that gets higher as your hand gets closer, and the light gets brighter. The centre button switches the instrument on and off.

## Step by step
1. A variable **playing** (0 or 1) switched by the centre button.
2. In the "sensors updated" event (prox): if playing is 1 and the middle sensor sees something (value above 1000)…
3. … play a note whose frequency is 200 + middle sensor value ÷ 10, for 6 (1/60 s).
4. Light the top LED with a red intensity of middle sensor value ÷ 150.

## Hints
1. Arithmetic blocks are in **Math**: put the sensor value inside a "÷" block, then inside a "+" block.
2. The sensor value goes from about 0 (far) to 4500 (very close): 200 + 4500 ÷ 10 = 650 Hz.
3. Use "set LED RGB" with a calculated red value: the result must stay between 0 and 32.

## To go further
Use the left sensor for the note and the right sensor for the volume (duration), like a real theremin with two antennas.
''', scripts=[[set_var('playing', 0)],
              [on_button('center', if_(compare(get_var('playing'), 'EQ', 0), [set_var('playing', 1), led('#00ff00')],
                                       [set_var('playing', 0), led_off()]))],
              [on_update('prox', if_(logic(compare(get_var('playing'), 'EQ', 1), 'AND', compare(prox_value('middle'), 'GT', 1000)),
                                     [note(arith(200, '+', arith(prox_value('middle'), '/', 10)), 6),
                                      led_rgb(arith(prox_value('middle'), '/', 150), 0, 0)]))]]))

HEAD = ('<!DOCTYPE aesl-source>\n<network>\n\n<!--list of global events-->\n\n<!--list of constants-->\n\n'
        '<!--show keywords state-->\n<keywords flag="true"/>\n\n<!--node thymio-II-->\n<node nodeId="51938" name="thymio-II">\n\n')
for a in A:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    md = (f"---\ntitle: {a['title']}\nlevel: {a['level']}\nage: {AGE[a['level']]}\nneeds: {a['needs']}\n"
          f"author: {OWN}\n---\n" + a['md'].strip() + '\n')
    open(os.path.join(d, 'activity.md'), 'w', encoding='utf-8').write(md)
    xml = '<xml xmlns="http://www.w3.org/1999/xhtml">' + ''.join(
        xml_stack(s, 40 + (i % 2) * 380, 40 + (i // 2) * 220) for i, s in enumerate(a['scripts'])) + '</xml>'
    # The Aseba code part is filled in by check_blockly.py (Blockly generates it).
    text = HEAD + '__CODE__' + '\n\n<toolsPlugins>\n<ThymioBlockly>\n' + xml + '\n</ThymioBlockly>\n</toolsPlugins>\n</node>\n\n</network>'
    open(os.path.join(d, 'solution.aesl'), 'w', encoding='utf-8').write(text)
print('\n'.join(sorted(os.listdir(ROOT))))
