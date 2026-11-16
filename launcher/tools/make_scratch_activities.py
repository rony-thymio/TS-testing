#!/usr/bin/env python3
"""Writes the Scratch activities (activities/scratch/<id>/activity.md + project.json).

Activities 01-07 come from "Thymio et Scratch" by Joël Rivet and Didier Roy (Stripes Edizioni),
adapted into English; 08 (no sheet in the material received) gets its challenge written from the
book's solution. 09 and 10 are new activities written for Thymio Suite.
project.json is turned into solution.sb3 by tools/build_sb3.py (Scratch itself saves the file).
Run from launcher/:  python3 tools/make_scratch_activities.py && python3 tools/build_sb3.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from scratchgen import *  # noqa

BOOK = 'Joël Rivet and Didier Roy, "Thymio et Scratch" (Stripes Edizioni), adapted into English'
BOOK_R = 'Joël Rivet, "Thymio et Scratch" (Stripes Edizioni), adapted into English'
OWN = 'Thymio Suite activities'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'activities', 'scratch')
AGE = {1: '8+', 2: '10+', 3: '12+'}
A = []

A.append(dict(id='01-first-blocks', title='First Thymio blocks', level=1, author=BOOK,
              needs='Nothing else needed', md='''
## The story
Before driving a robot car, you need to know its controls. Let's discover the Thymio blocks of Scratch one by one.

## Your goal
Thymio drives slowly with blue lights. When something comes close in front of it, it stops and turns red.

## Step by step
1. Drag the block **horiz. prox. sensor (2)** into the script area and click it: a number appears. Bring a finger close to Thymio's middle sensor and click again. What are the smallest and largest values?
2. Click the **motor (all) speed (50)** block: Thymio starts! Find the block that stops it.
3. Click the **LEDs (all) R: 32 G: 0 B: 0** block and try other colours. Find the block that switches the lights off.
4. Now build the script: **when green flag clicked**, **forever**, **if** the middle sensor is above 2000, red light and stop the motors, **else** blue light and speed 50.

## Hints
1. The `if … else` block is in the orange "Control" category; the `>` block is in the green "Operators" category.
2. The middle sensor is number 2 in the list of horizontal sensors.
3. Without `forever`, Thymio checks its sensor only once, at the very beginning.

## To go further
Thymio is now a self-driving car. If a pedestrian crosses in front of it, it must stop, then drive off again once the pedestrian has passed. Does your script already do that? Add a sound when it stops.
''', scripts=[[when_flag(), forever(if_else(gt(prox('centre'), 2000),
                                               [leds('all', 32, 0, 0), stop_motors()],
                                               [leds('all', 0, 0, 32), motor('all', 50)]))]]))

A.append(dict(id='02-museum', title='Thymio at the museum', level=1, author=BOOK,
              needs='A few objects (the "statues") on a table or the floor', md='''
## The story
Thymio visits the museum of Thymioville, which is being rebuilt. Statues and objects are standing everywhere, and Thymio must not knock them over!

## Your goal
Thymio drives through the museum. When a statue appears on one side, it turns away; when a statue is right in front of it, it stops until the way is free.

## Step by step
1. **Read the script**: when the middle sensor sees nothing (below 1000), Thymio drives at speed 50.
2. If it sees an obstacle on the left (above 2000), it turns right; on the right, it turns left.
3. The original script backs away when something is right in front. **Change it** so that Thymio stops instead, and drives off again when the statue is gone.
4. Write in plain words what your script does, using "if … then …".

## Hints
1. Turning right means: the left wheel goes faster than the right one (left 75, right 0).
2. The `if … else` around the whole script decides between "the way is free" and "something is in front".
3. To stop, replace the two "backing away" motor blocks by **stop motors**.

## To go further
Make Thymio light up orange while it waits in front of a statue.
''', scripts=[[when_flag(), forever(if_else(lt(prox('centre'), 1000),
                                               [motor('all', 50),
                                                if_(gt(prox('left'), 2000), motor('left', 75), motor('right', 0)),
                                                if_(gt(prox('right'), 2000), motor('left', 0), motor('right', 75))],
                                               [stop_motors()]))]]))

A.append(dict(id='03-under-control', title='Thymio under control', level=1, author=BOOK,
              needs='Nothing else needed (a pen and a sheet of paper to draw letters, if you like)', md='''
## The story
Thymio is your remote-controlled car: first with its own buttons, then with the computer keyboard.

## Your goal
Drive Thymio with its 5 buttons, then with the arrow keys and the space bar of the keyboard.

## Step by step
1. The block **when button (center) pressed** is a "hat" block: the blocks under it run whenever the button is pressed. No green flag needed!
2. Forward button: speed 50. Backward button: speed -50.
3. Left button: turn left (left wheel slow, right wheel fast). Right button: turn right.
4. Centre button: stop.
5. Now do the same with the keyboard: replace the button hats by **when (up arrow) key pressed** blocks (space bar to stop).

## Hints
1. Each button gets its own little script: 5 scripts in total.
2. To turn left: left wheel 15, right wheel 50. To turn right: the other way round.
3. The "when key pressed" block is in the yellow "Events" category.

## To go further
Make a joke on a friend: put the button scripts and the keyboard scripts together (10 scripts), let your friend drive with the buttons… then press the keys to do the opposite!
''', scripts=[
    [when_button('left'), motor('left', 15), motor('right', 50)],
    [when_button('right'), motor('left', 50), motor('right', 15)],
    [when_button('front'), motor('all', 50)],
    [when_button('back'), motor('all', -50)],
    [when_button('center'), stop_motors()],
    [when_key('up arrow'), motor('all', 50)],
    [when_key('down arrow'), motor('all', -50)],
    [when_key('left arrow'), motor('left', 15), motor('right', 50)],
    [when_key('right arrow'), motor('left', 50), motor('right', 15)],
    [when_key('space'), stop_motors()]]))

A.append(dict(id='04-sos-toxic-gas', title='SOS toxic gas', level=1, author=BOOK_R,
              needs='A large sheet of white paper (A3 or bigger) and a pen in Thymio\'s hole', md='''
## The story
"I'm stuck in the robotics building: toxic gas has spread from the factory next door! Luckily I'm next to the giant Thymio we finished building yesterday. I'll send it onto the roof to write SOS. The rescue team's drone will surely see it… but first I'll test my program on a sheet of paper with a small Thymio."

## Your goal
Thymio writes the letters S, O, S on the paper with a pen, without lifting the pen.

## Step by step
1. Put a pen in Thymio's hole and place it on a big sheet of paper.
2. Draw an **S** with two arcs of circle: one turning one way, one turning the other way.
3. Draw a line to the next letter, an **O** (a full circle), then a line to the last letter.
4. Draw the last **S**.
5. Make one custom block per letter in "My Blocks", and call them from the main script.

## Hints
1. The block **move in a circle radius (60) angle (-150)** draws an arc; a negative angle turns the other way.
2. **move (80)** draws a straight line (in millimetres).
3. Custom blocks: "My Blocks" → "Make a Block", name it S, and put its blocks under "define S".
4. Letters are linked by a line at the top or at the bottom, so the pen never has to be lifted.

## To go further
Write your own name, or add sounds and lights so the giant Thymio is noticed from far away.

## For the teacher
A good opportunity to introduce custom blocks (procedures). Encourage students to draw the path on paper before programming it.
''', scripts=[
    [when_flag(), call('S'), call('line-O-line'), call('last S')],
    define('S', arc(60, -150), arc(60, 130)),
    define('line-O-line', move(80), arc(120, 390), move(240)),
    define('last S', turn(180), arc(60, -150), arc(60, 150))]))

A.append(dict(id='05-dizzy-thymio', title='Dizzy Thymio', level=2, author=BOOK_R,
              needs='Some free space on the floor or a table', md='''
## The story
Thymio plays at spinning on the spot, faster and faster… until it gets dizzy! Then it slows down, groans, and takes a rest.

## Your goal
Thymio spins on itself, faster and faster and redder and redder, until it reaches a top speed. It then plays a sound 4 times, slows down little by little until it stops, and goes quiet.

## Step by step
1. Create two variables: **speed** (starting at 20) and **colour** (starting at 0).
2. **Repeat until** speed is above 155: left wheel at 0 − speed, right wheel at speed, red light = colour, wait 0.2 s, then add 5 to speed and 0.5 to colour.
3. **Repeat 4 times**: play system sound 4 and wait 0.5 s.
4. **Repeat until** speed = 0: the same loop, but adding −5 to speed and −0.5 to colour.
5. Wait 3 seconds, play system sound 5, and switch everything off.

## Hints
1. Variables are in the orange "Variables" category: "set … to" and "change … by".
2. To spin on the spot, the two wheels turn at the same speed in opposite directions: "0 − speed" gives the opposite of speed.
3. Use the variable colour as the R value of the LED block, so the red grows with the speed.

## To go further
Make Thymio spin the other way when it slows down, or let the user choose the top speed with the arrow keys.
''', scripts=[[when_flag(), set_var('colour', 0), set_var('speed', 20),
                repeat_until(gt(var('speed'), 155), motor('left', sub_(0, var('speed'))), motor('right', var('speed')),
                             leds('all', var('colour'), 0, 0), wait(0.2), change_var('speed', 5), change_var('colour', 0.5)),
                repeat(4, system_sound(4), wait(0.5)),
                repeat_until(eq(var('speed'), 0), motor('left', sub_(0, var('speed'))), motor('right', var('speed')),
                             leds('all', var('colour'), 0, 0), wait(0.2), change_var('speed', -5), change_var('colour', -0.5)),
                wait(3), system_sound(5), clear_leds(), leds_temperature(0, 0), leds_ground(0, 0), stop_motors()]]))

A.append(dict(id='06-maze', title='The maze', level=2, author=BOOK_R,
              needs='A maze made of walls (about 25 paper walls), with passages wide enough for Thymio', md='''
## The story
Thymio is trapped in a maze. The simplest way out: follow a wall, always on the same side, without ever letting go of it.

## Your goal
Thymio follows the wall on its left until it gets out of the maze. Pressing the space bar stops the program.

## Step by step
1. First write the algorithm in plain words: if there is a wall in front, turn right; otherwise, if there is a wall on the left, keep going; if there is no wall on the left, turn left.
2. Thymio never really goes straight: if it sees the left wall, it turns slightly right; if not, it turns slightly left. That keeps it along the wall.
3. Build the script with **repeat until (space) key pressed**, and **stop motors** at the end.

## Hints
1. Test the middle sensor **or** the left sensor in the same `if`: in both cases, move away from the wall.
2. Slightly right: left wheel 40, right wheel 10. Slightly left: left wheel 10, right wheel 40.
3. Thymio cannot know that it is out of the maze: that's why the space bar stops it.

## To go further
This only works if the maze has no "island" (walls in the middle not connected to the outside walls). Why?

## For the teacher
Build one maze for the whole class. If Thymio touches a wall, the wall must not move.
''', scripts=[[when_flag(), repeat_until(key_pressed('space'),
                                             if_else(or_(gt(prox('centre'), 1500), gt(prox('left'), 1500)),
                                                     [motor('left', 40), motor('right', 10)],
                                                     [motor('left', 10), motor('right', 40)])),
                stop_motors()]]))

A.append(dict(id='07-ambulance', title='Thymio ambulance', level=2, author=BOOK_R, robots='2 or more',
              needs='2 robots (or more): one ambulance, one or more taxis', md='''
## The story
Thymio has become an ambulance with an injured person on board. It races to the hospital, sirens blaring. Unfortunately a taxi is slow to clear the road and Thymio has to stop… until, hearing the siren, the taxi pulls over to the right and frees the way.

## Your goal
Program the ambulance and the taxi. The ambulance drives at full speed with its siren, stops behind the taxi, and drives off again when the road is clear. The taxi waits until it hears the siren, then moves out of the way.

## Step by step
1. **Ambulance, script 1**: forever, play the notes D (294 Hz) and A (440 Hz), one second each, with a pause.
2. **Ambulance, script 2**: forever, drive at speed 150, wait until something is close in front, stop, then wait until the way is free again.
3. **Taxi** (the second robot, its own project): wait until the sound level is above 10, then make an S-shaped move to the right with two arcs of circle.
4. Load the ambulance project on one robot and the taxi project on the other.

## Hints
1. Two scripts under the same green flag run at the same time: one for the siren, one for the driving.
2. **wait until** is in the orange "Control" category; use the middle sensor with `>` 2500 to stop and `<` 1500 to start again.
3. The taxi uses the **sound intensity** block and **move in a circle radius (250) angle (60)**, then angle −60.

## To go further
Several teams can each program a taxi: line them up along the ambulance's route.

## For the teacher
The solution opens two projects: the ambulance and the taxi. Each needs its own robot (open the second one with another robot selected).
''', scripts=[
    [when_flag(), forever(note(294, 1), wait(1), note(440, 1), wait(1))],
    [when_flag(), forever(motor('all', 150), wait_until(gt(prox('centre'), 2500)), stop_motors(),
                          wait_until(lt(prox('centre'), 1500)))]],
              extra={'solution-taxi': [[when_flag(), wait_until(gt(mic(), 10)), arc(250, 60), arc(250, -60)]]}))

A.append(dict(id='08-light-piano', title='Light piano', level=1, author=OWN,
              needs='Nothing else needed', md='''
## The story
Thymio becomes a musical instrument: each key of the keyboard plays a note and lights Thymio up in its own colour.

## Your goal
Pressing the keys 1 to 5 plays the notes C, D, E, F, G on Thymio, each with its own colour.

## Step by step
1. Use **when (1) key pressed**: play a note at 262 Hz for 0.3 s and light up red.
2. Key 2: 294 Hz, orange. Key 3: 330 Hz, yellow. Key 4: 349 Hz, green. Key 5: 392 Hz, blue.
3. Play a tune you know!

## Hints
1. One small script per key, each starting with a "when key pressed" hat.
2. Orange is R 32, G 16, B 0; yellow is R 32, G 32, B 0.
3. The note block is **play note at (262) Hz during (0.3) s**.

## To go further
Add the keys 6, 7, 8 for A (440 Hz), B (494 Hz) and the high C (523 Hz), and use the Thymio buttons for drums with the system sounds.
''', scripts=[
    [when_key('1'), leds('all', 32, 0, 0), note(262, 0.3)],
    [when_key('2'), leds('all', 32, 16, 0), note(294, 0.3)],
    [when_key('3'), leds('all', 32, 32, 0), note(330, 0.3)],
    [when_key('4'), leds('all', 0, 32, 0), note(349, 0.3)],
    [when_key('5'), leds('all', 0, 0, 32), note(392, 0.3)]]))

A.append(dict(id='09-shape-artist', title='Shape artist', level=1, author=OWN,
              needs='A large sheet of paper and a pen in Thymio\'s hole', md='''
## The story
Thymio takes up drawing. With a pen in its hole, it can draw any shape made of straight lines and turns.

## Your goal
Thymio draws a square when you press the forward button, and a triangle when you press the backward button.

## Step by step
1. Under **when button (front) pressed**: repeat 4 times "move 100" and "turn 90".
2. Under **when button (back) pressed**: repeat 3 times "move 100" and "turn 120".
3. Put a pen in Thymio's hole and try both shapes.

## Hints
1. The angles of a full turn always add up to 360°: 4 × 90 for a square, 3 × 120 for a triangle.
2. **repeat (4)** is in the orange "Control" category.
3. If the shape does not close perfectly, the floor may be slippery: try on a sheet of paper on a table.

## To go further
Draw a hexagon (6 sides) and a star (5 points, turn 144° each time). Which angle gives a circle?
''', scripts=[
    [when_button('front'), repeat(4, move(100), turn(90))],
    [when_button('back'), repeat(3, move(100), turn(120))]]))

A.append(dict(id='10-parking-assistant', title='Parking assistant', level=3, author=OWN,
              needs='A box or a wall to park in front of', md='''
## The story
Modern cars help their drivers to park: the closer the wall, the faster the beeps. Thymio gets its own parking assistant, with the screen as the car's dashboard.

## Your goal
Thymio moves slowly towards a wall. On the screen, the sprite shows the distance; Thymio beeps faster and faster as the wall gets closer, and stops at the right moment.

## Step by step
1. Create a variable **distance** and, forever, set it to the value of the middle sensor.
2. On the screen, make the sprite **say** "Closeness: " followed by the value.
3. While the value is below 3000, drive at speed 40 and beep: a short note, then a pause that gets shorter as the value grows.
4. When the value reaches 3000, stop, light up red and say "Parked!".

## Hints
1. The sensor value grows when the wall gets closer: about 0 far away, about 4500 very close.
2. A pause that shrinks: wait (4000 − distance) / 4000 seconds.
3. Use **join** (green "Operators" category) to put a text and a number together in the speech bubble.

## To go further
Add a green, orange and red light depending on the distance, like on a real dashboard.
''', scripts=[
    [when_flag(), forever(set_var('distance', prox('centre')), say(join('Closeness: ', var('distance'))))],
    [when_flag(), leds('all', 0, 32, 0),
     repeat_until(gt(var('distance'), 3000), motor('all', 40), note(880, 0.05),
                  wait(div_(sub_(4000, var('distance')), 4000))),
     stop_motors(), leds('all', 32, 0, 0), wait(0.5), say('Parked!')]]))

for a in A:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    front = ['---', f"title: {a['title']}", f"level: {a['level']}", f"age: {AGE[a['level']]}", f"needs: {a['needs']}"]
    if a.get('robots'):
        front.append(f"robots: {a['robots']}")
    front += [f"author: {a['author']}", '---']
    open(os.path.join(d, 'activity.md'), 'w', encoding='utf-8').write('\n'.join(front) + '\n' + a['md'].strip() + '\n')
    projects = {'solution': a['scripts'], **a.get('extra', {})}
    for name, scripts in projects.items():
        blocks, variables = build(scripts)
        json.dump({'blocks': blocks, 'variables': variables}, open(os.path.join(d, name + '.json'), 'w'), indent=1)
print('\n'.join(sorted(os.listdir(ROOT))))
