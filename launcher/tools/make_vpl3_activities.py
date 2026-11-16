#!/usr/bin/env python3
"""Writes the VPL3 activities of the library (activities/vpl3/<id>/activity.md + solution.vpl3).

Source: "Teacher introduction with classroom activities" – VPL3 teacher guide, EPFL (Mobots)
and HEP-Vaud, 2020-2021, translated by Mobsya. Missions and solutions follow the guide;
activities 04, 06, 07 and 10 turn guide missions or "to go further" ideas into full activities.
Run from launcher/:  python3 tools/make_vpl3_activities.py

Block parameters (VPL3 "basic" blocks, as in Thymio Suite 2.4.0):
  move: 0 stop, 1 forward, 2 forward-right, 3 spin right, 5 backward, 7 spin left, 8 forward-left
  top color 8: 0 off, 1 red, 2 green, 3 yellow, 4 blue, 5 magenta, 6 cyan, 7 white
  ground [left, right]: -1 sees black (or nothing), 1 sees white, 0 ignored
  horiz prox [middle, front-left, front-right, left, right, back-left, back-right]: 1 something, -1 nothing, 0 ignored
  button 1: 0 centre, 1 forward, 2 backward, 3 right, 4 left
"""
import json, os

AUTHOR = 'VPL3 teacher guide by EPFL (Mobots) and HEP-Vaud, translated by Mobsya'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'activities', 'vpl3')
BASIC = ["init", "button 1", "acc side", "acc upside down", "tap", "ground mean", "ground", "horiz prox",
         "color 8 state", "bottom color 8 state", "state 256", "move", "top color 8", "bottom color 8",
         "set state 256", "notes"]
NOTES = [0, 1, 1, 1, 2, 1, 0, 1, 2, 1, 4, 2]      # the guide's default tune
ALARM = [4, 1, 2, 1, 4, 1, 2, 1, 4, 1, 2, 2]


def B(name, param):
    return {"name": name, "disabled": False, "locked": False, "param": param}


def R(*blocks):
    return {"blocks": list(blocks), "disabled": False, "locked": False}


AGE = {1: '6+', 2: '8+', 3: '10+'}
A = []

A.append(dict(id='01-blue-light', title='Blue light', level=1, needs='Nothing else needed', md='''
## The story
Your first program! Thymio wakes up and says hello with its lights.

## Your goal
When you launch the program, Thymio lights up in blue on its top.

## Step by step
1. Find the **start** event: the orange block with a "play" triangle.
2. Drag it into the first line, on the left of the arrow.
3. Find the **top light** action and drag it on the right of the arrow.
4. Choose blue, then press the green play button at the top of VPL3.

## Hints
1. A line always reads: "when this happens → do that".
2. The start event happens only once, when you press play.
3. Click the colours in the light block until blue is selected.

## To go further
Try every colour. Can you make Thymio white?
''', program=[R(B("init", []), B("top color 8", [4]))]))

A.append(dict(id='02-remote-control', title='Remote control', level=1, needs='Nothing else needed', md='''
## The story
Thymio is a little car, and its buttons are the remote control.

## Your goal
When you touch the forward button, Thymio moves forward. When you touch the centre button, it stops.

## Step by step
1. Use the **buttons** event and select the forward arrow.
2. Next to it, put the **motors** action with the arrow pointing forward.
3. Make a second line: the centre button, with the motors stopped.
4. Run the program and drive Thymio with its buttons.

## Hints
1. The buttons event is the block that shows Thymio's five buttons.
2. In the motors block, the square in the middle means "stop".
3. Each line works on its own: one line per button.

## To go further
Add lines for the backward, left and right buttons to drive Thymio everywhere.
''', program=[R(B("button 1", [1]), B("move", [1])), R(B("button 1", [0]), B("move", [0]))]))

A.append(dict(id='03-traffic-light-hand', title='Traffic-light hand', level=1, needs='Nothing else needed', md='''
## The story
Thymio is a traffic light that watches the road in front of it.

## Your goal
When Thymio detects something in front of it (a hand, for example), it lights up green. When it detects nothing, it lights up red.

## Step by step
1. Use the **front sensors** event and select only the middle sensor.
2. In one line, the sensor "detects something": choose green for the top light.
3. In a second line, the same sensor "detects nothing": choose red.
4. Run the program and move your hand slowly towards Thymio.

## Hints
1. Click a sensor once or twice to switch between "detects something" and "detects nothing".
2. Leave the other sensors untouched: they are ignored.
3. The two lines are opposite: one for each case.

## To go further
At what distance does the light change? Measure it with a ruler, then try with a black object.
''', program=[R(B("horiz prox", [1, 0, 0, 0, 0, 0, 0]), B("top color 8", [2])),
              R(B("horiz prox", [-1, 0, 0, 0, 0, 0, 0]), B("top color 8", [1]))]))

A.append(dict(id='04-who-is-behind', title="Who's behind me?", level=1, needs='Nothing else needed', md='''
## The story
Thymio cannot see behind its back… or can it? It has two sensors at the back too.

## Your goal
When Thymio detects something behind it, it plays a little tune and lights up magenta.

## Step by step
1. Use the **sensors** event and select the back left sensor (detects something).
2. Add the **music** action and the top light in magenta.
3. Make a second line for the back right sensor, with the same actions.
4. Run the program and put your hand behind Thymio.

## Hints
1. The back sensors are the two small squares at the bottom of the sensors block.
2. One line per back sensor, because each line reacts when all its sensors match.
3. Click the notes in the music block to change the tune.

## To go further
Compose your own tune: high notes for the left sensor, low notes for the right one.
''', program=[R(B("horiz prox", [0, 0, 0, 0, 0, 1, 0]), B("notes", NOTES), B("top color 8", [5])),
              R(B("horiz prox", [0, 0, 0, 0, 0, 0, 1]), B("notes", NOTES), B("top color 8", [5]))]))

A.append(dict(id='05-table-edge', title="Don't fall off the table", level=1, needs='A light-coloured table. Keep a hand ready the first time!', md='''
## The story
Thymio explores the table, but it must not fall off!

## Your goal
When the program starts, Thymio moves forward. As soon as it reaches the edge of the table, it stops.

## Step by step
1. Start event → motors forward.
2. Use the **ground sensors** event: over the edge, both sensors see nothing below them.
3. In that case, stop the motors.
4. Test slowly, with a hand ready to catch Thymio.

## Hints
1. Over the edge, the ground sensors react exactly as if they saw black.
2. Select both ground sensors on black in the same block.
3. Two lines are enough: one to start, one to stop.

## To go further
Instead of stopping, make Thymio back up and turn, so it can keep exploring.
''', program=[R(B("init", []), B("move", [1])), R(B("ground", [-1, -1]), B("move", [0]))]))

A.append(dict(id='06-upside-down', title='Help, I fell over!', level=2, needs='Nothing else needed', md='''
## The story
Thymio has fallen on its back like a turtle and calls for help.

## Your goal
When you place Thymio on its back, it plays an alarm and lights up red. When you put it back on its wheels and touch the centre button, the light goes off.

## Step by step
1. Find the **upside down** event (Thymio turned over).
2. Add a tune and a red top light.
3. Make a second line: centre button → light off.
4. Run the program, then turn Thymio over gently.

## Hints
1. The upside-down event uses the accelerometer, the sensor that feels which way is down.
2. "Off" is the black square in the colour block.
3. Turn Thymio over slowly: the program sends the alarm while it lies on its back.

## To go further
Use the "tap" event too: when you knock on Thymio, it lights up yellow.
''', program=[R(B("acc upside down", []), B("notes", ALARM), B("top color 8", [1])),
              R(B("button 1", [0]), B("top color 8", [0]))]))

A.append(dict(id='07-explore-enclosure', title='Explore the enclosure', level=2, needs='An enclosure made of walls (books or cardboard), about 1 m wide', md='''
## The story
Thymio is a cleaning robot. It must visit the whole room without getting stuck against the walls.

## Your goal
Thymio drives around an enclosure: it turns away from the walls it detects and keeps exploring.

## Step by step
1. Start event → move forward.
2. Wall on the left side → turn forward-right.
3. Wall on the right side → turn forward-left.
4. Wall right in front → spin on the spot.
5. Nothing in front or on the sides → move forward again.

## Hints
1. The sensors block has five sensors at the front: left side, front left, middle, front right, right side.
2. Use one line per case and select only the sensors that matter for that case.
3. The "nothing around" line needs all front sensors on "detects nothing".
4. Put a felt-tip pen in Thymio's hole to see where it has been.

## To go further
Change the colour of the walls (white, then dark grey): does Thymio see them as well? Why?
''', program=[R(B("init", []), B("move", [1])),
              R(B("horiz prox", [0, 0, 0, 1, 0, 0, 0]), B("move", [2])),
              R(B("horiz prox", [0, 0, 0, 0, 1, 0, 0]), B("move", [8])),
              R(B("horiz prox", [1, 0, 0, 0, 0, 0, 0]), B("move", [3])),
              R(B("horiz prox", [-1, -1, -1, -1, -1, 0, 0]), B("move", [1]))]))

A.append(dict(id='08-line-follower', title='Line follower', level=2, needs='A black track on white paper (tracks A, B and C of the guide)', md='''
## The story
Thymio is a train, and the black track is its rail.

## Your goal
Program Thymio to follow a black track, in both directions.

## Step by step
1. Thymio sees the track with its two ground sensors. Each one sees black or white.
2. That makes four cases: black-black, black-white, white-black and white-white.
3. Give each case its own movement: straight on, slightly left, slightly right, or turning on the spot.
4. Test on track A (straight), then track B, then the loop of track C.

## Hints
1. Both sensors on black: Thymio is on the track, go straight.
2. Only the left sensor on black: the track is on the left, turn slightly left.
3. Both sensors on white: Thymio has lost the track; spin on the spot to find it again.

## To go further
Track C in both directions: does your program work clockwise and anticlockwise?
''', program=[R(B("ground", [-1, -1]), B("move", [1])), R(B("ground", [-1, 1]), B("move", [8])),
              R(B("ground", [1, -1]), B("move", [2])), R(B("ground", [1, 1]), B("move", [3]))]))

A.append(dict(id='09-thymio-tale', title="Thymio's tale", level=3, needs="Track D of the guide, with characters next to the marks", md='''
## The story
Thymio travels along a path and meets characters on the way: a story told by a robot!

## Your goal
Thymio moves along the track. Each time it comes across a character (a small black mark), it plays a tune and lights up.

## Step by step
1. Follow the edge of the line with only the left ground sensor.
2. Keep the right sensor free to notice the small marks next to the line.
3. When both sensors see black, play a tune and light up green.
4. Place characters next to each mark and tell your story.

## Hints
1. Left sensor on black (right ignored) → forward-right; left sensor on white → forward-left. Thymio zigzags along the edge.
2. The marks are under the right sensor only.
3. Both sensors on black means "a mark": add the music and colour actions in that line.

## To go further
Make Thymio stop at each character for a moment before continuing (see the next activity).
''', program=[R(B("ground", [-1, 0]), B("move", [2])),
              R(B("ground", [-1, -1]), B("notes", NOTES), B("top color 8", [2])),
              R(B("ground", [1, 0]), B("move", [8]))]))

A.append(dict(id='10-stop-for-characters', title='Stop for the characters', level=3, needs='A black line and a few characters (figurines) placed beside it', md='''
## The story
On its journey, Thymio stops politely in front of each character, says hello, and waits until the character leaves.

## Your goal
Thymio follows a line. When a character stands on its right side, it stops and plays a tune; when the character is removed, it continues on its way.

## Step by step
1. Follow the edge of the line with the left ground sensor, as in "Thymio's tale".
2. Add a condition: only move when the right side sensor detects nothing.
3. When the right side sensor detects something, stop and play a tune.
4. Remove the character: Thymio continues.

## Hints
1. A line can have several events: VPL3 then waits until all of them are true.
2. Combine the ground sensors event and the front sensors event in the same line.
3. The right side sensor is the one at the far right of the sensors block.

## To go further
Use a different colour for each case so you can follow what Thymio "thinks".
''', program=[R(B("ground", [-1, 0]), B("horiz prox", [0, 0, 0, 0, -1, 0, 0]), B("move", [2])),
              R(B("ground", [1, 0]), B("horiz prox", [0, 0, 0, 0, -1, 0, 0]), B("move", [8])),
              R(B("horiz prox", [0, 0, 0, 0, 1, 0, 0]), B("move", [0]), B("notes", NOTES))]))

for a in A:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    md = (f"---\ntitle: {a['title']}\nlevel: {a['level']}\nage: {AGE[a['level']]}\nneeds: {a['needs']}\n"
          f"author: {AUTHOR}\n---\n" + a['md'].strip() + '\n')
    open(os.path.join(d, 'activity.md'), 'w', encoding='utf-8').write(md)
    obj = {"basicBlocks": BASIC, "basicMultiEvent": True,
           "disabledUI": ["src:language", "vpl:exportToHTML", "vpl:flash"], "program": a['program'], "code": None}
    json.dump(obj, open(os.path.join(d, 'solution.vpl3'), 'w'), indent=1)
print('\n'.join(sorted(os.listdir(ROOT))))
