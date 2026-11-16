# Solution: Don't stay there!
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
turning = False
threshold = 2500
speed = 150
motor_left_target = speed
motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target, timer_period, leds_top, turning

    if prox_ground_delta[0] < 400 and prox_ground_delta[1] < 400: # on the black circle
        turning = True
        timer_period[0] = 3000
        leds_top = RED
        motor_left_target = 100
        motor_right_target = -100
    else:
        if turning == False:
            if prox_horizontal[0] > threshold or prox_horizontal[1] > threshold:
                leds_top = GREEN            # object on the left: face it
                motor_left_target = 0
                motor_right_target = speed
            else:
                if prox_horizontal[3] > threshold or prox_horizontal[4] > threshold:
                    leds_top = BLUE         # object on the right: face it
                    motor_left_target = speed
                    motor_right_target = 0
                else:
                    leds_top = [32, 32, 0]  # nothing: straight on
                    motor_left_target = speed
                    motor_right_target = speed

@onevent
def timer0():
    global timer_period, turning, leds_top
    timer_period[0] = 0
    turning = False # back to normal after 3 s, so Thymio has time to turn
    leds_top = BLACK
