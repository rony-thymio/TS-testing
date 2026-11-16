# Don't stay there!
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Thymio pushes the objects out of the black circle one after the other, without leaving the circle itself.
#
# STEP BY STEP
# 1. Inside the circle, Thymio drives straight ahead (yellow light).
# 2. If it sees an object on one side, it turns towards it to face it (green or blue light), then pushes it.
# 3. When both ground sensors reach the black circle, Thymio turns on the spot for 3 seconds to come back inside (red light), ignoring its front sensors during that time.
# 4. Thymio is not expected to stop on its own once the arena is clean.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

turning = False
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
