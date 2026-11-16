# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
# Solution: Self-driving car
speed = 250
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

    if prox_ground_delta[0] < 400 or prox_ground_delta[1] < 400: # black line: U-turn
        half_turn = True
        timer_period[0] = 1800
        motor_left_target = speed
        motor_right_target = -speed

@onevent
def timer0():
    global timer_period, half_turn

    half_turn = False # the U-turn is over: follow the walls again
    timer_period[0] = 0
