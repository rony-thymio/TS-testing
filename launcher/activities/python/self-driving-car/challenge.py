# Self-driving car
# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
#
# THE CHALLENGE
# A self-driving car must move safely on the road. Our model only uses its
# 5 front sensors. The road is a winding street lined with walls; the end of
# the street is a black strip on the ground, where Thymio makes a U-turn.
# An object can be placed in the street as a pedestrian: Thymio must stop in
# front of it and wait until it is removed before driving on.
# Walls: thick A4 sheets folded in four along their length.
#
# To run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? Click "Hints" on the activity in Thymio Suite.

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period
    # your code here
    pass

@onevent
def timer0():
    global timer_period
    # your code here
    pass
