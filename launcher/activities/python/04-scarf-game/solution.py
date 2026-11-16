# Solution: The scarf game
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
speed = 100
gap = 10

def color_random():
    """one random colour among 12, to tell the robots apart"""
    global leds_top
    n = math_rand() // 5462 + 6
    if n == 0:
        leds_top = [32, 32, 32] # white
    elif n == 1:
        leds_top = [0, 16, 32] # sky blue
    elif n == 2:
        leds_top = [0, 32, 0] # green
    elif n == 3:
        leds_top = [0, 32, 8] # emerald green
    elif n == 4:
        leds_top = [0, 32, 32] # cyan
    elif n == 5:
        leds_top = [8, 32, 0] # fluo green
    elif n == 6:
        leds_top = [32, 0, 0] # red
    elif n == 7:
        leds_top = [32, 0, 8] # fuchsia
    elif n == 8:
        leds_top = [32, 0, 32] # magenta
    elif n == 9:
        leds_top = [32, 16, 0] # orange
    elif n == 10:
        leds_top = [32, 32, 0] # yellow
    else:
        leds_top = [12, 4, 0] # maroon

color_random()

@onevent
def button_center():
    global motor_left_target, motor_right_target
    motor_left_target = 0
    motor_right_target = 0

@onevent
def button_forward():
    global motor_left_target, motor_right_target, speed
    speed += gap
    motor_left_target = speed
    motor_right_target = speed

@onevent
def button_backward():
    global motor_left_target, motor_right_target, speed
    speed += gap
    motor_left_target = -speed
    motor_right_target = -speed

@onevent
def button_left():
    global motor_left_target, motor_right_target
    motor_left_target = 0
    motor_right_target = speed

@onevent
def button_right():
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = 0

@onevent
def prox():
    global speed, motor_left_target, motor_right_target
    if prox_horizontal[5] > 2500 or prox_horizontal[6] > 2500: # scarf lost
        speed = 0
        motor_left_target = 0
        motor_right_target = 0
        nf_sound_freq(1000, 180)

@onevent
def rc5():
    global motor_left_target, motor_right_target
    if rc5_command == 85:   # left key: turn left
        motor_left_target = 0
        motor_right_target = speed
    if rc5_command == 87:   # centre key: stop
        motor_left_target = 0
        motor_right_target = 0
    if rc5_command == 86:   # right key: turn right
        motor_left_target = speed
        motor_right_target = 0
    if rc5_command == 80:   # up key: forward
        motor_left_target = speed
        motor_right_target = speed
    if rc5_command == 81:   # down key: backward
        motor_left_target = -speed
        motor_right_target = -speed
