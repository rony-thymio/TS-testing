# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
# Solution: The maze (left-hand rule)
threshold = 2000  # a wall is detected above this value
speed = 150
motor_left_target = speed
motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target

    if prox_horizontal[0] > threshold:   # wall on the left: move gently away
        motor_left_target = speed
        motor_right_target = speed // 2
    else:                                # no wall on the left: move gently towards it
        motor_left_target = speed // 2
        motor_right_target = speed

    if prox_horizontal[2] > threshold:   # wall in front: turn right
        motor_left_target = speed
        motor_right_target = 0
