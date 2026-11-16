# Solution: The Thymio relay
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
# Program 2: ALL THE OTHER robots of the relay.
speed = 100
nf_leds_top(0, 0, 0)

@onevent
def prox():
    global motor_left_target, motor_right_target, speed

    if prox_horizontal[5] > 2000 or prox_horizontal[6] > 2000: # the previous robot arrives: go
        motor_left_target = speed
        motor_right_target = speed
        nf_leds_top(32, 0, 16)

    if prox_horizontal[2] > 2000: # the next robot is in front: stop
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)

    if prox_ground_delta[0] < 400: # black finish line: stop
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)
