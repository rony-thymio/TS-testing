#!/usr/bin/env python3
"""Writes the Aseba activities (activities/aseba/<id>/activity.md + solution.aesl).

New activities written for Thymio Suite, for the Aseba text editor of the suite.
Run from launcher/:  python3 tools/make_aseba_activities.py
"""
import os
from xml.sax.saxutils import escape

OWN = 'Thymio Suite activities'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'activities', 'aseba')
AGE = {1: '12+', 2: '14+', 3: '14+'}
A = []

A.append(dict(id='01-traffic-light', title='Traffic light', level=1, needs='Nothing else needed', md='''
## The story
Your first Aseba program: Thymio becomes a traffic light that you control with its buttons.

## Your goal
Forward button: green. Centre button: orange. Backward button: red. The left and right buttons switch the light off.

## Step by step
1. Write `onevent button.forward`: the lines below it run when the forward button changes.
2. Check that the button is pressed with `if button.forward == 1 then … end`.
3. Inside, set the colour with `call leds.top(0, 32, 0)` (red, green, blue: 0 to 32).
4. Do the same for the other buttons, then click ▶ Run.

## Hints
1. Each button has its own event: `button.forward`, `button.backward`, `button.left`, `button.right`, `button.center`.
2. The event also runs when the button is released (value 0): that is why the `if … == 1` is needed.
3. Orange is a lot of red and a little green: `call leds.top(32, 12, 0)`.

## To go further
Make the light change by itself, green → orange → red, with a timer (see "Light chaser").
''', code='''# Traffic light controlled with the buttons
onevent button.forward
    if button.forward == 1 then
        call leds.top(0, 32, 0)      # green
    end

onevent button.center
    if button.center == 1 then
        call leds.top(32, 12, 0)     # orange
    end

onevent button.backward
    if button.backward == 1 then
        call leds.top(32, 0, 0)      # red
    end

onevent button.left
    if button.left == 1 then
        call leds.top(0, 0, 0)       # off
    end

onevent button.right
    if button.right == 1 then
        call leds.top(0, 0, 0)       # off
    end
'''))

A.append(dict(id='02-distance-light', title='Distance light', level=1, needs='Nothing else needed', md='''
## The story
Thymio cannot measure distances in centimetres, but its sensors tell how much infrared light comes back: the closer an object, the bigger the value.

## Your goal
The closer your hand to Thymio's middle sensor, the brighter its red light.

## Step by step
1. Open the **Variables** panel and watch `prox.horizontal[2]` while you move your hand: note the smallest and largest values.
2. Write `onevent prox`: it runs 10 times per second with fresh sensor values.
3. Divide the sensor value so that it fits between 0 and 32, and use it as the red value of `leds.top`.

## Hints
1. The value goes from about 0 (nothing) to about 4500 (touching): 4500 / 150 = 30.
2. Calculations are allowed inside `call`: `call leds.top(prox.horizontal[2] / 150, 0, 0)`.
3. Aseba only uses whole numbers: 100 / 150 gives 0.

## To go further
Show the distance on the circle of 8 LEDs around the buttons, like a gauge.
''', code='''# The closer the hand, the brighter the red light
onevent prox
    call leds.top(prox.horizontal[2] / 150, 0, 0)
'''))

A.append(dict(id='03-avoid-obstacles', title='Avoid obstacles', level=1, needs='A few objects or walls', md='''
## The story
Thymio explores the room on its own, like a robot vacuum cleaner, and turns away from everything in its way.

## Your goal
Thymio drives forward. When something is in front, it turns on the spot until the way is free.

## Step by step
1. Start the motors when the program starts: `motor.left.target = 200` and `motor.right.target = 200` at the top, outside any event.
2. In `onevent prox`, test the middle sensor: above 2000 means an obstacle.
3. Obstacle: turn on the spot (one wheel forward, the other backward). No obstacle: drive forward.
4. Stop with the centre button.

## Hints
1. Lines outside any `onevent` run once, when you click ▶ Run.
2. `if … then … else … end` chooses between the two cases.
3. Turning on the spot: `motor.left.target = 200` and `motor.right.target = -200`.

## To go further
Turn left if the obstacle is on the right (sensor 4) and right if it is on the left (sensor 0).
''', code='''# Drive and turn away from obstacles
motor.left.target = 200
motor.right.target = 200

onevent prox
    if prox.horizontal[2] > 2000 then
        motor.left.target = 200      # obstacle: turn on the spot
        motor.right.target = -200
    else
        motor.left.target = 200      # free: straight on
        motor.right.target = 200
    end

onevent button.center
    if button.center == 1 then
        motor.left.target = 0
        motor.right.target = 0
    end
'''))

A.append(dict(id='04-light-chaser', title='Light chaser', level=2, needs='Nothing else needed', md='''
## The story
Fairground lights chase each other in a circle. Thymio has 8 orange LEDs around its buttons: let's make a light run round and round.

## Your goal
One LED of the circle lights up at a time and moves on every 150 ms, forever. The forward and backward buttons make it faster or slower.

## Step by step
1. Declare a variable `pos` (the lit LED, 0 to 7) and an array `circle[8]`.
2. Start timer 0: `timer.period[0] = 150`.
3. In `onevent timer0`: switch the old LED off in the array, move `pos` on by 1 (back to 0 after 7), switch the new one on, then `call leds.circle(...)` with the 8 values.
4. Forward button: shorter period (faster). Backward button: longer period (slower).

## Hints
1. Declare arrays at the top: `var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]`.
2. `pos = (pos + 1) % 8` goes 0, 1, … 7, 0, 1…
3. `call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])`.
4. Keep the period between 30 and 1000 ms.

## To go further
Make a "comet": the LED behind the lit one stays half bright.
''', code='''# A light running round the circle of 8 LEDs
var pos = 0
var period = 150
var circle[8] = [32, 0, 0, 0, 0, 0, 0, 0]

timer.period[0] = period

onevent timer0
    circle[pos] = 0
    pos = (pos + 1) % 8
    circle[pos] = 32
    call leds.circle(circle[0], circle[1], circle[2], circle[3], circle[4], circle[5], circle[6], circle[7])

onevent button.forward
    if button.forward == 1 and period > 40 then
        period = period - 20         # faster
        timer.period[0] = period
    end

onevent button.backward
    if button.backward == 1 and period < 1000 then
        period = period + 20         # slower
        timer.period[0] = period
    end
'''))

A.append(dict(id='05-music-box', title='Music box', level=2, needs='Nothing else needed', md='''
## The story
Thymio has a little loudspeaker. With two arrays (the notes and their lengths) it can play any tune.

## Your goal
When you press the centre button, Thymio plays "Ode to Joy" (the first 8 notes), one note after the other.

## Step by step
1. Store the frequencies in an array `notes[8]` and the lengths in `durations[8]` (in 1/60 s).
2. A variable `index` remembers which note is playing.
3. Centre button: `index = 0` and play the first note with `call sound.freq(…)`.
4. `onevent sound.finished` runs when a note ends: move to the next note, until the end of the array.

## Hints
1. Ode to Joy starts E E F G G F E D: 330, 330, 349, 392, 392, 349, 330, 294 Hz.
2. 20/60 s is a short note; 40/60 s a long one.
3. In `sound.finished`, only play the next note if `index < 8`, otherwise the tune would never stop.

## To go further
Add a light per note (one colour for each pitch), or a second tune on the forward button.
''', code='''# Plays the first notes of "Ode to Joy" (Beethoven)
var notes[8] = [330, 330, 349, 392, 392, 349, 330, 294]
var durations[8] = [20, 20, 20, 20, 20, 20, 20, 40]
var index = 8

onevent button.center
    if button.center == 1 then
        index = 0
        call sound.freq(notes[index], durations[index])
    end

onevent sound.finished
    index = index + 1
    if index < 8 then
        call sound.freq(notes[index], durations[index])
    end
'''))

A.append(dict(id='06-follow-me', title='Follow me', level=2, needs='A flat surface and your hand (or a book)', md='''
## The story
Thymio is a faithful little dog: it follows your hand, but never bumps into it.

## Your goal
Thymio keeps a fixed distance from your hand: it moves forward when the hand is far, backward when it is too close, and waits when the distance is right.

## Step by step
1. Choose a target value for the middle sensor, for example 2500.
2. In `onevent prox`, compute the error: `target - prox.horizontal[2]`.
3. The speed is the error divided by a number: big error, fast; small error, slow.
4. If nothing at all is seen (value 0), stop: there is no hand to follow.

## Hints
1. Hand too far: the value is small, the error positive, Thymio moves forward. Too close: negative error, it backs away.
2. Try `speed = (2500 - prox.horizontal[2]) / 8`.
3. This is called a **proportional controller**: robots use it everywhere.

## To go further
Also use the left and right sensors so that Thymio turns to follow your hand sideways.
''', code='''# Keeps a fixed distance from your hand (proportional controller)
var target = 2500
var speed

onevent prox
    if prox.horizontal[2] == 0 then
        speed = 0                                # no hand: wait
    else
        speed = (target - prox.horizontal[2]) / 8
    end
    motor.left.target = speed
    motor.right.target = speed
'''))

A.append(dict(id='07-smooth-line-follower', title='Smooth line follower', level=2, needs='A black line (4 cm wide) on white paper', md='''
## The story
A simple line follower zigzags. Real robots steer smoothly: the further they drift from the line, the more they turn.

## Your goal
Thymio follows a black line by steering in proportion to the difference between its two ground sensors.

## Step by step
1. Watch `prox.ground.delta` in the **Variables** panel: about 800 on white, below 400 on black.
2. Place Thymio with the line between its two sensors: each sensor sees half black, half white.
3. Compute `difference = prox.ground.delta[0] - prox.ground.delta[1]`.
4. Left wheel = base speed + difference / k, right wheel = base speed − difference / k.

## Hints
1. Start with a base speed of 100 and k = 4, then adjust.
2. If Thymio turns the wrong way, swap the signs.
3. Follow one edge of the line (half on black, half on white), not its middle.

## To go further
Make the base speed higher on straight lines (small difference) and lower in bends.
''', code='''# Proportional line follower: follows the edge of a black line
var base = 100
var difference

onevent prox
    difference = prox.ground.delta[0] - prox.ground.delta[1]
    motor.left.target = base + difference / 4
    motor.right.target = base - difference / 4
'''))

A.append(dict(id='08-guard-robot', title='Guard robot', level=3, needs='Nothing else needed', md='''
## The story
Thymio guards a treasure. It sleeps, wakes up when you knock on it, watches all around, and sounds the alarm if anyone approaches.

## Your goal
Program a robot with three states: **asleep** (blue, quiet), **watching** (green, for 10 seconds) and **alarm** (red, siren).

## Step by step
1. A variable `state`: 0 asleep, 1 watching, 2 alarm. Start asleep.
2. Asleep: a knock on Thymio (`onevent tap`) switches to watching and starts a 10-second timer.
3. Watching: if any front or back sensor sees something, switch to alarm.
4. When the timer ends while watching, go back to sleep.
5. Alarm: siren until you press the centre button, which puts the guard back to sleep.

## Hints
1. Write one small piece of code per state change, and set the colour at the same time.
2. Use a loop over the 7 sensors: `for i in 0:6 do … end`.
3. Stop a timer with `timer.period[0] = 0`.
4. A repeating siren: in `onevent sound.finished`, play the next note again while `state == 2`.

## To go further
Count the intruders and show the number on the circle LEDs.
''', code='''# Guard robot: 0 asleep (blue), 1 watching (green), 2 alarm (red)
var state = 0
var i
var seen

call leds.top(0, 0, 32)

onevent tap
    if state == 0 then
        state = 1
        call leds.top(0, 32, 0)
        timer.period[0] = 10000      # watch for 10 s
    end

onevent prox
    if state == 1 then
        seen = 0
        for i in 0:6 do
            if prox.horizontal[i] > 2000 then
                seen = 1
            end
        end
        if seen == 1 then
            state = 2
            timer.period[0] = 0
            call leds.top(32, 0, 0)
            call sound.freq(880, 20)
        end
    end

onevent timer0
    if state == 1 then
        state = 0                    # nobody came: back to sleep
        timer.period[0] = 0
        call leds.top(0, 0, 32)
    end

onevent sound.finished
    if state == 2 then
        call sound.freq(880, 20)     # siren continues
    end

onevent button.center
    if button.center == 1 then
        state = 0
        call leds.top(0, 0, 32)
    end
'''))

A.append(dict(id='09-random-explorer', title='Dice robot', level=3, needs='Some free space on the floor', md='''
## The story
Thymio cannot decide where to go… so it rolls a die! Every two seconds it picks a random movement and a random colour.

## Your goal
Every 2 seconds Thymio chooses at random between: forward, turn left, turn right, or stop, and shows a matching colour. The centre button stops the game.

## Step by step
1. Start timer 0 with a period of 2000 ms.
2. In `onevent timer0`, get a random number with `call math.rand(r)`.
3. Turn it into a number from 0 to 3, and choose the movement with `if … elseif …`.
4. Avoid obstacles anyway: in `onevent prox`, stop if something is very close.

## Hints
1. `math.rand` gives a number between -32768 and 32767. `abs r % 4` gives 0, 1, 2 or 3.
2. `elseif` lets you test several cases one after the other.
3. Stop the game by setting `timer.period[0] = 0` and the motors to 0.

## To go further
Give "forward" a bigger chance than the other movements, so Thymio explores further.
''', code='''# Every 2 seconds, a random movement and colour
var r
var choice

timer.period[0] = 2000

onevent timer0
    call math.rand(r)
    choice = abs r % 4
    if choice == 0 then
        motor.left.target = 200          # forward, green
        motor.right.target = 200
        call leds.top(0, 32, 0)
    elseif choice == 1 then
        motor.left.target = -150         # turn left, blue
        motor.right.target = 150
        call leds.top(0, 0, 32)
    elseif choice == 2 then
        motor.left.target = 150          # turn right, yellow
        motor.right.target = -150
        call leds.top(32, 32, 0)
    else
        motor.left.target = 0            # pause, white
        motor.right.target = 0
        call leds.top(32, 32, 32)
    end

onevent prox
    if prox.horizontal[2] > 3000 then
        motor.left.target = 0
        motor.right.target = 0
    end

onevent button.center
    if button.center == 1 then
        timer.period[0] = 0
        motor.left.target = 0
        motor.right.target = 0
        call leds.top(0, 0, 0)
    end
'''))

A.append(dict(id='10-leader-follower', title='Leader and followers', level=3, robots='2 or more on the same dongle',
              needs='2 or more wireless robots paired to the same dongle (see "Pair wireless robots")', md='''
## The story
A team of robots works together: the leader decides, the followers obey. In Aseba, robots on the same dongle can send **events** to each other.

## Your goal
When you press a button on the leader robot, all the robots of the group show the same colour and drive the same way.

## Step by step
1. In the **Events** panel of the Aseba editor, create a global event `order` with 1 value.
2. Leader: in each button event, `emit order [n]` with a number for the order (1 forward, 2 left, 3 right, 0 stop) and obey it yourself.
3. Followers: `onevent order` reads the number in `event.args[0]` and applies it.
4. Open the Aseba editor with all the robots: each robot has its own tab. Write the leader program in the first tab and the follower program in the others, then click "Run all".

## Hints
1. All robots on the same dongle form a group and share the global events.
2. A subroutine avoids writing the same code twice: `sub apply` … then `callsub apply`.
3. `emit` sends the event to the other robots, not to the sender: the leader must also obey its own order.

## To go further
Make the followers answer: each one emits `ready` when it has obeyed, and the leader counts the answers.
''', events=[('order', 1)], nodes=['''# LEADER: sends an order to all the robots of the group
var command = 0

sub apply
    if command == 1 then
        motor.left.target = 150
        motor.right.target = 150
        call leds.top(0, 32, 0)
    elseif command == 2 then
        motor.left.target = -100
        motor.right.target = 100
        call leds.top(0, 0, 32)
    elseif command == 3 then
        motor.left.target = 100
        motor.right.target = -100
        call leds.top(32, 32, 0)
    else
        motor.left.target = 0
        motor.right.target = 0
        call leds.top(32, 0, 0)
    end

onevent button.forward
    if button.forward == 1 then
        command = 1
        emit order [command]
        callsub apply
    end

onevent button.left
    if button.left == 1 then
        command = 2
        emit order [command]
        callsub apply
    end

onevent button.right
    if button.right == 1 then
        command = 3
        emit order [command]
        callsub apply
    end

onevent button.center
    if button.center == 1 then
        command = 0
        emit order [command]
        callsub apply
    end
''', '''# FOLLOWER: obeys the orders of the leader
onevent order
    if event.args[0] == 1 then
        motor.left.target = 150
        motor.right.target = 150
        call leds.top(0, 32, 0)
    elseif event.args[0] == 2 then
        motor.left.target = -100
        motor.right.target = 100
        call leds.top(0, 0, 32)
    elseif event.args[0] == 3 then
        motor.left.target = 100
        motor.right.target = -100
        call leds.top(32, 32, 0)
    else
        motor.left.target = 0
        motor.right.target = 0
        call leds.top(32, 0, 0)
    end
''']))


def aesl(events, nodes):
    s = '<!DOCTYPE aesl-source>\n<network>\n\n\n<!--list of global events-->\n'
    for name, size in events:
        s += f'<event size="{size}" name="{name}"/>\n'
    s += '\n\n<!--list of constants-->\n\n\n<!--show keywords state-->\n<keywords flag="true"/>\n\n\n'
    for i, code in enumerate(nodes):
        s += f'<!--node thymio-II-->\n<node nodeId="{i + 1}" name="thymio-II">{escape(code)}</node>\n\n\n'
    return s + '</network>\n'


for a in A:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    front = ['---', f"title: {a['title']}", f"level: {a['level']}", f"age: {AGE[a['level']]}", f"needs: {a['needs']}"]
    if a.get('robots'):
        front.append(f"robots: {a['robots']}")
    front += [f'author: {OWN}', '---']
    open(os.path.join(d, 'activity.md'), 'w', encoding='utf-8').write('\n'.join(front) + '\n' + a['md'].strip() + '\n')
    open(os.path.join(d, 'solution.aesl'), 'w', encoding='utf-8').write(aesl(a.get('events', []), a.get('nodes') or [a['code']]))
print('\n'.join(sorted(os.listdir(ROOT))))
