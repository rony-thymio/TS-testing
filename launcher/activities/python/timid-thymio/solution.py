# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
# Solution: Timid Thymio
speed = 200

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
