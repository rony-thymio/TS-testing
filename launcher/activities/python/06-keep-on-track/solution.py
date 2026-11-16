# Solution: Keep on track
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
leds_top = [0, 0, 0]
speed = 150
motor_left_target = speed
motor_right_target = speed
gap = 1

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top, speed
    if prox_ground_delta[0] < 400:
        if prox_ground_delta[1] < 400: # black black: straight on, blue
            motor_left_target = speed
            motor_right_target = speed
            leds_top = [0, 0, 32]
        else:                          # black white: turn left, green
            motor_left_target = 0
            motor_right_target = speed
            leds_top = [0, 32, 0]
    else:
        if prox_ground_delta[1] < 400: # white black: turn right, yellow
            motor_left_target = speed
            motor_right_target = 0
            leds_top = [32, 32, 0]
        else:                          # white white: U-turn, red, faster
            motor_left_target = speed
            motor_right_target = -speed
            leds_top = [32, 0, 0]
            speed += gap
            print(speed)
