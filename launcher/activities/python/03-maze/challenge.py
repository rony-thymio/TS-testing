# The maze
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Program Thymio to get out of the maze with the "left-hand rule": it follows the wall on its left until it finds the exit.
#
# STEP BY STEP
# 1. Thymio drives forward from the start.
# 2. If it gets too close to the left wall, it steers gently away from it.
# 3. If it moves away from the left wall, it steers gently back towards it.
# 4. If there is a wall in front, it turns right.
# 5. Adjust the detection threshold and the speeds until Thymio gets out every time.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

threshold = 2000
speed = 150

@onevent
def prox():
    global motor_left_target, motor_right_target
    # your code here
