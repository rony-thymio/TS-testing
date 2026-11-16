# Solution: The maze
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
threshold = 2000  # a wall is detected above this value
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
