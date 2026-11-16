# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
# Solution: Thymio the explorer
stop = True
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

    if prox_ground_delta[0] < 400: # the void (edge of the table)
        speed = 0
        motor_left_target = speed
        motor_right_target = speed
        leds_top = BLACK
