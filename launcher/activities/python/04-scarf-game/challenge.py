# The scarf game
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Drive your Thymio with the buttons or the remote control. If anything is detected by one of its back sensors, your robot has lost.
#
# STEP BY STEP
# 1. The forward, backward, left and right buttons (or remote keys) move the robot; the centre button stops it.
# 2. When a back sensor (prox_horizontal[5] or [6]) detects something, the robot must: set its speed to 0, stop both motors, and play a high sound for 3 seconds.
# 3. Give each robot a random colour at the start, so players can tell them apart.
# 4. Agree on the same back-sensor threshold for all robots: it is only fair!
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

speed = 100

@onevent
def button_forward():
    global motor_left_target, motor_right_target
    # your code here

@onevent
def prox():
    global speed, motor_left_target, motor_right_target
    # your code here
