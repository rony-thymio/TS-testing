# Solution: The Thymio relay
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
# Program 1: the FIRST robot of the relay.
# The program for the other robots is in the other file: …-solution-others.py
speed = 100
nf_leds_top(32, 16, 0)

@onevent
def button_forward():
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = speed

@onevent
def prox():
    global motor_left_target, motor_right_target, speed
    if prox_horizontal[2] > 3000: # the next robot is in front: stop
        speed = 0
        motor_left_target = 0
        motor_right_target = 0
        nf_leds_top(0, 0, 0)
