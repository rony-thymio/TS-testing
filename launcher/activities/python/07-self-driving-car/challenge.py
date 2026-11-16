# Self-driving car
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Thymio drives along a winding street lined with walls. It stops in front of a pedestrian until the pedestrian is gone, and makes a U-turn on the black strip at the end of the street.
#
# STEP BY STEP
# 1. With nothing around, Thymio drives straight ahead.
# 2. If a wall comes close on one side, Thymio steers gently away from it.
# 3. If something is right in front (a pedestrian), Thymio stops and waits until it is removed.
# 4. On the black strip at the end of the street, Thymio turns on the spot for about 2 seconds to make its U-turn, then drives on.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

speed = 250
half_turn = False

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, half_turn
    # your code here

@onevent
def timer0():
    global timer_period, half_turn
    # your code here
