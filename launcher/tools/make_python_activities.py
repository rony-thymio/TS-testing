#!/usr/bin/env python3
"""Writes the Python activities of the library (activities/python/<id>/).

Source: Joël Rivet, "Programmer Thymio avec Python et Thonny", session 1 activity book
(licence CC BY-NC), adapted into English for Thymio Suite. Each activity gets:
  activity.md   texts shown in the library and the challenge window
  challenge.py  starter file (the challenge as comments + an empty skeleton)
  solution.py   (+ solution-*.py when several robots need different programs)
Run from launcher/:  python3 tools/make_python_activities.py
"""
import os, re, textwrap

AUTHOR = 'Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English'
ROOT = os.path.join(os.path.dirname(__file__), '..', 'activities', 'python')

A = []

A.append(dict(id='01-timid-thymio', title='Timid Thymio', level=1, needs='Nothing else needed', md='''
## The story
Thymio is a shy little robot. It does not like being surprised: when something comes close, it moves away, and if it is trapped on all sides it panics!

## Your goal
Recreate the red "scared" behaviour that is built into Thymio, with your own Python program.

## Step by step
1. If Thymio sees nothing around it, it stays still.
2. If something appears at the **front left**, Thymio backs away while turning to the right. At the **front right**, it backs away turning to the left.
3. If something appears at the **back left**, Thymio moves forward while turning to the right. At the **back right**, it moves forward turning to the left.
4. If something is right in front of it, Thymio backs straight away.
5. If Thymio is surrounded (front and back), it stops, lights up red and plays system sound 4.

## Hints
1. Put everything in one event: `@onevent def prox():` runs about 10 times per second with fresh sensor values.
2. Start the event by stopping both motors and switching the light off: that is the "nothing around" case. The `if` blocks that follow change it when needed.
3. Sensors: `prox_horizontal[0]` front left, `[2]` front middle, `[4]` front right, `[5]` back left, `[6]` back right. A value above 2000 means something is close.
4. Write the "surrounded" test last, so that it wins over all the others. You can ignore front sensors 1 and 3.

## To go further
Use a different colour for each case, so you can see which rule Thymio is following.
''', skeleton='''@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top
    # your code here
''', solutions={'solution.py': '''speed = 200

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top

    # nothing around
    motor_left_target = 0
    motor_right_target = 0
    leds_top = BLACK

    if prox_horizontal[0] > 2000: # something at the front left
        motor_left_target = -speed
        motor_right_target = 0

    if prox_horizontal[4] > 2000: # something at the front right
        motor_left_target = 0
        motor_right_target = -speed

    if prox_horizontal[6] > 2000:
        if prox_horizontal[5] < 1000: # something at the back right only
            motor_left_target = 0
            motor_right_target = speed
        else:                         # something at the back left and right
            motor_left_target = speed
            motor_right_target = speed

    if prox_horizontal[5] > 2000: # something at the back left
        motor_left_target = speed
        motor_right_target = 0

    if prox_horizontal[2] > 2000:
        if prox_horizontal[5] > 2000 or prox_horizontal[6] > 2000: # front and back: surrounded
            motor_left_target = 0
            motor_right_target = 0
            nf_sound_system(4)
            leds_top = RED
        else:                                                      # front only
            motor_left_target = -speed
            motor_right_target = -speed
'''}))

A.append(dict(id='02-explorer', title='Thymio the explorer', level=1, needs='A table and a few objects heavy enough not to be pushed', md='''
## The story
Thymio lands on an unknown planet (your table) covered with rocks of all sizes. It must explore without bumping into anything, and above all without falling off the edge of the world!

## Your goal
Thymio drives around the table, avoids each obstacle by going around it on the left or on the right, and stops at the edge of the table.

## Step by step
1. Thymio waits. When you touch the forward button, it starts driving. The centre button stops it.
2. While driving, compare what the left sensors and the right sensors see: turn away from the side that sees more.
3. If something is right in front, turn anyway.
4. If a ground sensor sees nothing below it (the edge of the table), stop for good.

## Hints
1. Use a variable `stop` (True or False) set by the buttons, and leave `prox()` straight away when it is True: `if stop: return`.
2. Add the two left sensors together and the two right sensors together: `p_left = prox_horizontal[0] + prox_horizontal[1]` and `p_right = prox_horizontal[3] + prox_horizontal[4]`.
3. If `p_left > p_right` the obstacle is on the left: turn right. And the other way round.
4. The edge of the table: `prox_ground_delta[0] < 400` means nothing below the left ground sensor. If you cannot use a table, a black area on the floor works too.

## To go further
Give each case its own colour (going straight, turning left, turning right, stopped at the edge).
''', skeleton='''stop = True
speed = 150

@onevent
def button_forward():
    global stop
    # your code here

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top
    if stop: return
    # your code here
''', solutions={'solution.py': '''stop = True
speed = 150
motor_left_target = 0
motor_right_target = 0

@onevent
def button_forward():
    global motor_left_target, motor_right_target, stop
    stop = False
    motor_left_target = speed
    motor_right_target = speed

@onevent
def button_center():
    """extra button to stop the robot"""
    global motor_left_target, motor_right_target, stop
    stop = True
    motor_left_target = 0
    motor_right_target = 0

@onevent
def prox():
    global motor_left_target, motor_right_target, speed, leds_top, stop

    if stop: return

    p_left = prox_horizontal[0] + prox_horizontal[1]
    p_right = prox_horizontal[3] + prox_horizontal[4]
    p_center = prox_horizontal[2]

    if p_center > 3500:
        motor_left_target = -speed // 2 # turn left
        motor_right_target = speed
    else:
        if p_left > p_right:
            motor_left_target = speed # turn right
            motor_right_target = -speed // 2
        elif p_left < p_right:
            motor_left_target = -speed // 2 # turn left
            motor_right_target = speed
        else:
            motor_left_target = speed
            motor_right_target = speed

    if prox_ground_delta[0] < 400: # the edge of the table
        speed = 0
        motor_left_target = speed
        motor_right_target = speed
        leds_top = BLACK
'''}))

A.append(dict(id='03-maze', title='The maze', level=2, needs='A simple maze made of paper walls', md='''
## The story
Thymio is lost in a maze. Luckily it knows an old explorers' trick: keep one hand on the wall and never let go. Following the wall, you are sure to reach the exit.

## Your goal
Program Thymio to get out of the maze with the "left-hand rule": it follows the wall on its left until it finds the exit.

## Step by step
1. Thymio drives forward from the start.
2. If it gets too close to the left wall, it steers gently away from it.
3. If it moves away from the left wall, it steers gently back towards it.
4. If there is a wall in front, it turns right.
5. Adjust the detection threshold and the speeds until Thymio gets out every time.

## Hints
1. Only the left sensor `prox_horizontal[0]` and the middle sensor `prox_horizontal[2]` are needed: ignore the right side.
2. To steer gently, keep both wheels turning but make one slower: for example `speed` and `speed // 2`.
3. Test the wall in front last, so it wins over the rest.
4. Success depends on the numbers: try thresholds between 1500 and 3000 and speeds between 100 and 200.

## To go further
The maze must be "perfect" (no island in the middle). Build one with an island: does the left-hand rule still work? Why?

## For the teacher
Paper walls: fold an A4 sheet three times along its length into a square tube and tape it (about 30 × 5 × 5 cm). Walls must be at least 5 cm high.
''', skeleton='''threshold = 2000
speed = 150

@onevent
def prox():
    global motor_left_target, motor_right_target
    # your code here
''', solutions={'solution.py': '''threshold = 2000  # a wall is detected above this value
speed = 150
motor_left_target = speed
motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target

    if prox_horizontal[0] > threshold:   # close to the left wall: move gently away
        motor_left_target = speed
        motor_right_target = speed // 2
    else:                                # far from the left wall: move gently towards it
        motor_left_target = speed // 2
        motor_right_target = speed

    if prox_horizontal[2] > threshold:   # wall in front: turn right
        motor_left_target = speed
        motor_right_target = 0
'''}))

A.append(dict(id='04-scarf-game', title='The scarf game', level=2, robots='2 to 5', needs='2 to 5 robots, a Thymio remote control, an arena (walls recommended)', md='''
## The story
An old scout game: two players face each other, each with a scarf tucked in their belt at the back. They circle around each other trying to grab the other's scarf. The first one to succeed wins. Let's play it with Thymios: the "scarf" is the pair of back sensors.

## Your goal
Drive your Thymio with the buttons or the remote control. If anything is detected by one of its back sensors, your robot has lost.

## Step by step
1. The forward, backward, left and right buttons (or remote keys) move the robot; the centre button stops it.
2. When a back sensor (`prox_horizontal[5]` or `[6]`) detects something, the robot must: set its speed to 0, stop both motors, and play a high sound for 3 seconds.
3. Give each robot a random colour at the start, so players can tell them apart.
4. Agree on the same back-sensor threshold for all robots: it is only fair!

## Hints
1. Use one event per button: `@onevent def button_forward():` and so on.
2. With the remote control, use `@onevent def rc5():` and test `rc5_command`: 80 up, 81 down, 85 left, 86 right, 87 centre (remote 1).
3. Losing: `nf_sound_freq(1000, 180)` plays a high note for 3 seconds (180 = 3 × 60).
4. A random number: `math_rand()` gives a value between -32768 and 32767; `math_rand() // 5462 + 6` gives 0 to 11, one number per colour.

## To go further
Each press of a button adds a little speed (a variable `gap`), for finer control. Play with walls: touching a wall with the back also loses!

## For the teacher
One remote controls every robot in the room, so robots must listen to different keys (robot 1: 87/85/86/81/80, robot 2: 2/1/3/5/6, robot 3: 8/7/9/0/16). With several robots, a referee starts the game and checks that nobody uses their hands.
''', skeleton='''speed = 100

@onevent
def button_forward():
    global motor_left_target, motor_right_target
    # your code here

@onevent
def prox():
    global speed, motor_left_target, motor_right_target
    # your code here
''', solutions={'solution.py': '''speed = 100
gap = 10

def color_random():
    """one random colour among 12, to tell the robots apart"""
    global leds_top
    n = math_rand() // 5462 + 6
    if n == 0:
        leds_top = [32, 32, 32] # white
    elif n == 1:
        leds_top = [0, 16, 32] # sky blue
    elif n == 2:
        leds_top = [0, 32, 0] # green
    elif n == 3:
        leds_top = [0, 32, 8] # emerald green
    elif n == 4:
        leds_top = [0, 32, 32] # cyan
    elif n == 5:
        leds_top = [8, 32, 0] # fluo green
    elif n == 6:
        leds_top = [32, 0, 0] # red
    elif n == 7:
        leds_top = [32, 0, 8] # fuchsia
    elif n == 8:
        leds_top = [32, 0, 32] # magenta
    elif n == 9:
        leds_top = [32, 16, 0] # orange
    elif n == 10:
        leds_top = [32, 32, 0] # yellow
    else:
        leds_top = [12, 4, 0] # maroon

color_random()

@onevent
def button_center():
    global motor_left_target, motor_right_target
    motor_left_target = 0
    motor_right_target = 0

@onevent
def button_forward():
    global motor_left_target, motor_right_target, speed
    speed += gap
    motor_left_target = speed
    motor_right_target = speed

@onevent
def button_backward():
    global motor_left_target, motor_right_target, speed
    speed += gap
    motor_left_target = -speed
    motor_right_target = -speed

@onevent
def button_left():
    global motor_left_target, motor_right_target
    motor_left_target = 0
    motor_right_target = speed

@onevent
def button_right():
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = 0

@onevent
def prox():
    global speed, motor_left_target, motor_right_target
    if prox_horizontal[5] > 2500 or prox_horizontal[6] > 2500: # scarf lost
        speed = 0
        motor_left_target = 0
        motor_right_target = 0
        nf_sound_freq(1000, 180)

@onevent
def rc5():
    global motor_left_target, motor_right_target
    if rc5_command == 85:   # left key: turn left
        motor_left_target = 0
        motor_right_target = speed
    if rc5_command == 87:   # centre key: stop
        motor_left_target = 0
        motor_right_target = 0
    if rc5_command == 86:   # right key: turn right
        motor_left_target = speed
        motor_right_target = 0
    if rc5_command == 80:   # up key: forward
        motor_left_target = speed
        motor_right_target = speed
    if rc5_command == 81:   # down key: backward
        motor_left_target = -speed
        motor_right_target = -speed
'''}))

A.append(dict(id='05-relay', title='The Thymio relay', level=2, robots='3 or more', needs='3 or more robots, a start line and a black finish line', md='''
## The story
A long distance must be covered, and no single Thymio is allowed to run it alone. Like runners in a relay race, the robots must pass on the baton: each one starts when the previous one arrives behind it.

## Your goal
The first Thymio waits on the start line; the others wait at equal distances along the track. Write two programs so the robots carry the relay to the finish line.

## Step by step
1. **Robot 1** starts when you touch its forward button, and stops when it sees the next robot in front of it.
2. **The other robots** start when their back sensors feel the previous robot arriving, and stop when they see the next robot in front.
3. The last robot stops on the black finish line.
4. Load program 1 on the first robot and program 2 on all the others.

## Hints
1. Each robot uses its front middle sensor (`prox_horizontal[2]`) and its two back sensors (`[5]` and `[6]`).
2. Program 2: if a back sensor sees something, start; if the front sensor sees something, stop.
3. The finish line: `prox_ground_delta[0] < 400` means the ground sensor is over black.
4. Everything depends on the thresholds: the robot behind must be detected before it bumps into the one in front. Try 2000 to 3000.

## To go further
Several teams can each bring one robot: agree together on the thresholds and the speed so the relay works with everybody's robot.
''', skeleton='''speed = 100

@onevent
def prox():
    global motor_left_target, motor_right_target
    # your code here
''', solutions={'solution.py': '''# Program 1: the FIRST robot of the relay.
# The program for the other robots is in the other file: …-solution-others.py
speed = 100
nf_leds_top(32, 16, 0)

@onevent
def button_forward():
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target, speed
    if prox_horizontal[2] > 3000: # the next robot is in front: stop
        speed = 0
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)
''', 'solution-others.py': '''# Program 2: ALL THE OTHER robots of the relay.
speed = 100
nf_leds_top(0, 0, 0)

@onevent
def prox():
    global motor_left_target, motor_right_target, speed

    if prox_horizontal[5] > 2000 or prox_horizontal[6] > 2000: # the previous robot arrives: go
        motor_left_target = speed
        motor_right_target = speed
        nf_leds_top(32, 0, 16)

    if prox_horizontal[2] > 2000: # the next robot is in front: stop
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)

    if prox_ground_delta[0] < 400: # black finish line: stop
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)
'''}))

A.append(dict(id='06-keep-on-track', title='Keep on track', level=2, needs='A black line about 4 cm wide on white paper, open at both ends', md='''
## The story
Why do trains have rails? Because a guide lets them go much faster without leaving their path. No rails for Thymio, but a black line on the ground will do.

## Your goal
Thymio follows a black line back and forth, a little faster each time, without "derailing".

## Step by step
1. Both ground sensors on black: go straight (blue light).
2. Only the left sensor on black: turn left (green light).
3. Only the right sensor on black: turn right (yellow light).
4. Both sensors on white: the end of the line is reached, make a U-turn (red light) and speed up by 1.
5. How long does Thymio last before it leaves the line?

## Hints
1. Everything goes in `@onevent def prox():` using `prox_ground_delta[0]` (left) and `prox_ground_delta[1]` (right).
2. Below 400 means black. Nest two `if` tests to get the four cases.
3. Speed up in the "white-white" case with `speed += gap`. Do not name your variable `step`: it is a reserved word, and Thonny will not tell you clearly.
4. `print(speed)` shows the speed in Thonny's shell each time it changes.

## To go further
Count the return trips. Make the bends tighter, or race two robots on a closed track starting from opposite sides.

## For the teacher
Lines must be at least 4 cm wide: a black marker (Posca) or 5 cm black tape. The line must stop with white paper at both ends.
''', skeleton='''speed = 150
gap = 1

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top, speed
    # your code here
''', solutions={'solution.py': '''leds_top = [0, 0, 0]
speed = 150
motor_left_target = speed
motor_right_target = speed
gap = 1

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top, speed
    if prox_ground_delta[0] < 400:
        if prox_ground_delta[1] < 400: # black black: straight on, blue
            motor_left_target = speed
            motor_right_target = speed
            leds_top = [0, 0, 32]
        else:                          # black white: turn left, green
            motor_left_target = 0
            motor_right_target = speed
            leds_top = [0, 32, 0]
    else:
        if prox_ground_delta[1] < 400: # white black: turn right, yellow
            motor_left_target = speed
            motor_right_target = 0
            leds_top = [32, 32, 0]
        else:                          # white white: U-turn, red, faster
            motor_left_target = speed
            motor_right_target = -speed
            leds_top = [32, 0, 0]
            speed += gap
            print(speed)
'''}))

A.append(dict(id='07-self-driving-car', title='Self-driving car', level=3, needs='Paper walls, a black strip on the ground, an object as a pedestrian', md='''
## The story
A self-driving car must move safely on the road: it watches the walls, the other cars and above all the pedestrians. Our model only uses its 5 front sensors.

## Your goal
Thymio drives along a winding street lined with walls. It stops in front of a pedestrian until the pedestrian is gone, and makes a U-turn on the black strip at the end of the street.

## Step by step
1. With nothing around, Thymio drives straight ahead.
2. If a wall comes close on one side, Thymio steers gently away from it.
3. If something is right in front (a pedestrian), Thymio stops and waits until it is removed.
4. On the black strip at the end of the street, Thymio turns on the spot for about 2 seconds to make its U-turn, then drives on.

## Hints
1. Walls: sensors 0 (left) and 4 (right). Pedestrian: sensor 2 (middle), above 4000.
2. Time the U-turn with a timer: `timer_period[0] = 1800` starts it, and `@onevent def timer0():` runs when the time is up. Set `timer_period[0] = 0` there to stop the timer.
3. During the U-turn Thymio still sees the walls and would steer away. Add a variable `half_turn`: put the wall tests inside `if not half_turn:`.
4. Set `half_turn = True` on the black strip and back to `False` in `timer0()`.

## To go further
Add a second pedestrian, or a "traffic light": a coloured object that makes Thymio wait.

## For the teacher
Walls: thick A4 sheets folded in four along their length. The black strip must cover the whole width of the street.
''', skeleton='''speed = 250
half_turn = False

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, half_turn
    # your code here

@onevent
def timer0():
    global timer_period, half_turn
    # your code here
''', solutions={'solution.py': '''speed = 250
half_turn = False # False: Thymio is not making its U-turn and follows the walls

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, half_turn

    if not half_turn:
        if prox_horizontal[2] < 4000: # no pedestrian
            if prox_horizontal[0] == 0 and prox_horizontal[4] == 0:
                motor_left_target = speed
                motor_right_target = speed
            else:
                if prox_horizontal[0] > 1500:
                    motor_left_target = speed
                    motor_right_target = speed // 2
                if prox_horizontal[4] > 1500:
                    motor_left_target = speed // 2
                    motor_right_target = speed
        else:                         # pedestrian: wait
            motor_left_target = 0
            motor_right_target = 0

    if prox_ground_delta[0] < 400 or prox_ground_delta[1] < 400: # black strip: U-turn
        half_turn = True
        timer_period[0] = 1800
        motor_left_target = speed
        motor_right_target = -speed

@onevent
def timer0():
    global timer_period, half_turn
    half_turn = False # the U-turn is over: follow the walls again
    timer_period[0] = 0
'''}))

A.append(dict(id='08-dont-stay-there', title="Don't stay there!", level=3, needs='A sheet of about 70 cm with a black circle (4 cm wide), 3 or 4 light objects', md='''
## The story
Thymio is the caretaker of a round arena, and visitors left their things everywhere. It must clean up by pushing every object out of the circle.

## Your goal
Thymio pushes the objects out of the black circle one after the other, without leaving the circle itself.

## Step by step
1. Inside the circle, Thymio drives straight ahead (yellow light).
2. If it sees an object on one side, it turns towards it to face it (green or blue light), then pushes it.
3. When both ground sensors reach the black circle, Thymio turns on the spot for 3 seconds to come back inside (red light), ignoring its front sensors during that time.
4. Thymio is not expected to stop on its own once the arena is clean.

## Hints
1. Two situations: inside the circle (look for objects) and on the black line (turn back). Test the line first.
2. On the line, start a 3-second timer (`timer_period[0] = 3000`) and use a variable `turning = True` that blocks the object detection.
3. In `@onevent def timer0():` set `turning = False` and stop the timer.
4. Objects on the left: sensors 0 or 1. On the right: sensors 3 or 4. Turn towards the side that sees something.

## To go further
Count the objects pushed out (each time Thymio reaches the line just after pushing), and play a little tune when the arena is clean.

## For the teacher
Objects should be light, not too dark, 3 to 10 cm wide. The circle covers almost the whole sheet.
''', skeleton='''turning = False
threshold = 2500
speed = 150

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, leds_top, turning
    # your code here

@onevent
def timer0():
    global timer_period, turning, leds_top
    # your code here
''', solutions={'solution.py': '''turning = False
threshold = 2500
speed = 150
motor_left_target = speed
motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, leds_top, turning

    if prox_ground_delta[0] < 400 and prox_ground_delta[1] < 400: # on the black circle
        turning = True
        timer_period[0] = 3000
        leds_top = RED
        motor_left_target = 100
        motor_right_target = -100
    else:
        if turning == False:
            if prox_horizontal[0] > threshold or prox_horizontal[1] > threshold:
                leds_top = GREEN            # object on the left: face it
                motor_left_target = 0
                motor_right_target = speed
            else:
                if prox_horizontal[3] > threshold or prox_horizontal[4] > threshold:
                    leds_top = BLUE         # object on the right: face it
                    motor_left_target = speed
                    motor_right_target = 0
                else:
                    leds_top = [32, 32, 0]  # nothing: straight on
                    motor_left_target = speed
                    motor_right_target = speed

@onevent
def timer0():
    global timer_period, turning, leds_top
    timer_period[0] = 0
    turning = False # back to normal after 3 s, so Thymio has time to turn
    leds_top = BLACK
'''}))

A.append(dict(id='09-landing', title='Landing', level=3, needs='Nothing else needed (hold Thymio about 50 cm above a light table)', md='''
## The story
Thymio is a spacecraft coming in to land. During the approach its instruments sound the alarm louder and louder; once it touches down safely, everything calms down.

## Your goal
Hold Thymio flat about 50 cm above the table and lower it slowly. The closer it gets, the redder and the higher-pitched it becomes. When it touches the table, it turns green and plays a low note for 2 seconds.

## Step by step
1. During the descent, read the ground sensors: the closer the table, the larger `prox_ground_delta`.
2. Turn that value into a red intensity (0 to 32) and into a note that gets higher (start from 440 Hz, the A).
3. Touching down is the `tap` event: switch to green and play a low note for 2 seconds.
4. After landing, the approach phase must stop: use a variable for the two phases.

## Hints
1. Use the average of the two ground sensors: `delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2`.
2. A note that rises: `nf_sound_freq(440 + delta, 10)`.
3. For the colour, try an affine function such as `delta // 30 + 7`, and only light up above a small threshold so the red does not come on too early.
4. A variable `contact` (0 in the air, 1 on the ground) set in `@onevent def tap():` lets `prox()` ignore everything after landing.

## To go further
Make a "crash" if Thymio comes down too fast: compare the value with the one measured just before.
''', skeleton='''contact = 0

@onevent
def prox():
    global contact
    # your code here

@onevent
def tap():
    global contact, leds_top
    # your code here
''', solutions={'solution.py': '''delta = 0
color = 0
height = 0
contact = 0
threshold = 4 # so that the red does not light up too early

@onevent
def prox():
    global delta, color, height, contact
    if contact == 0:
        delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2
        if delta > threshold:
            color = delta // 30 + 7
            nf_leds_top(color, 0, 0)
        height = 440 + delta
        nf_sound_freq(height, 10)

@onevent
def tap():
    global contact, leds_top
    contact = 1
    leds_top = [0, 32, 0]
    nf_sound_freq(55, 150)
'''}))

A.append(dict(id='10-secret-code', title='Secret start code', level=3, needs='Nothing else needed', md='''
## The story
Thymio guards a secret lab. It must refuse to drive for anyone who does not know the password.

## Your goal
Thymio only starts after the right sequence of 4 button presses. The same button can be used several times.

## Step by step
1. Give each button a number: 0 centre, 1 forward, 2 right, 3 backward, 4 left.
2. Store the secret code in a list, and the buttons typed in another list.
3. After the 4th press, compare the two lists.
4. Right code: green light, a short high note, and Thymio drives off.
5. Wrong code: red light and system sound 1 (the "switch off" sound).

## Hints
1. Use two lists, `code` (the secret) and `user` (the buttons typed), and a counter `index`.
2. Each button event runs twice: once when the finger presses, once when it is released. Start each event with `if button_forward == 1: return` to keep only one of them.
3. Aseba cannot compare two lists with a single `==`: compare them element by element in a `for` loop.
4. Put the comparison in a function `evaluate()` and call it when `index` reaches 3.

## To go further
Give the player 3 tries, then lock Thymio for 10 seconds with a timer.
''', skeleton='''code = [1, 2, 2, 0] # the secret code, choose your own
user = [-1] * 6
index = 0

@onevent
def button_forward():
    global user, index
    # your code here
''', solutions={'solution.py': '''# Button numbers: 0 centre, 1 forward, 2 right, 3 backward, 4 left
code = [1, 2, 2, 0] # secret code, chosen by the programmer
user = [-1] * 6     # buttons typed by the player
index = 0
index_max = 3
leds_top = BLUE
nf_sound_system(-1) # no sound when buttons are touched

def evaluate():
    global leds_top, motor_left_target, motor_right_target, index
    success = True
    for i in range(4):
        if code[i] != user[i]:
            success = False
    if success: # right code
        nf_sound_freq(880, 30)
        leds_top = GREEN
        motor_left_target = 150
        motor_right_target = 150
    else:       # wrong code
        leds_top = RED
        nf_sound_system(1)

@onevent
def button_center():
    global user, index
    if button_center == 1: return # act when the finger is released
    user[index] = 0
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_forward():
    global user, index
    if button_forward == 1: return
    user[index] = 1
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_right():
    global user, index
    if button_right == 1: return
    user[index] = 2
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_backward():
    global user, index
    if button_backward == 1: return
    user[index] = 3
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_left():
    global user, index
    if button_left == 1: return
    user[index] = 4
    if index == index_max:
        evaluate()
    else:
        index += 1
'''}))


def comment(md_text):
    out = []
    for line in md_text.strip().split('\n'):
        line = line.replace('**', '').replace('`', '')
        out.append('# ' + line if line.strip() else '#')
    return '\n'.join(out)


def section(md, name):
    m = re.search(r'^## ' + re.escape(name) + r'\n(.*?)(?=^## |\Z)', md, re.S | re.M)
    return m.group(1).strip() if m else ''


for a in A:
    d = os.path.join(ROOT, a['id'])
    os.makedirs(d, exist_ok=True)
    front = ['---', f"title: {a['title']}", f"level: {a['level']}", 'age: 14+', f"needs: {a['needs']}"]
    if a.get('robots'):
        front.append(f"robots: {a['robots']}")
    front += [f'author: {AUTHOR}', '---']
    md = '\n'.join(front) + '\n' + a['md'].strip() + '\n'
    open(os.path.join(d, 'activity.md'), 'w', encoding='utf-8').write(md)
    head = (f"# {a['title']}\n# {AUTHOR}\n#\n# YOUR GOAL\n{comment(section(a['md'], 'Your goal'))}\n#\n"
            f"# STEP BY STEP\n{comment(section(a['md'], 'Step by step'))}\n#\n"
            "# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.\n"
            "# Stuck? The challenge window shows hints, one at a time.\n\n")
    open(os.path.join(d, 'challenge.py'), 'w', encoding='utf-8').write(head + a['skeleton'])
    for name, code in a['solutions'].items():
        open(os.path.join(d, name), 'w', encoding='utf-8').write(f"# Solution: {a['title']}\n# {AUTHOR}\n{code}")
print('\n'.join(sorted(os.listdir(ROOT))))
