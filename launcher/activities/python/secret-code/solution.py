# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
# Solution: Secret start code
# Button numbers: 0 centre, 1 forward, 2 right, 3 backward, 4 left
code = [1, 2, 2, 0] # secret code, chosen by the programmer
user = [-1] * 6     # buttons typed by the player
index = 0
index_max = 3
leds_top = BLUE
nf_sound_system(-1) # no sound when buttons are touched

@onevent
def button_center():
    global user, index
    if button_center == 1: return # act when the finger is released
    user[index] = 0
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_forward():
    global user, index
    if button_forward == 1: return
    user[index] = 1
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_right():
    global user, index
    if button_right == 1: return
    user[index] = 2
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_backward():
    global user, index
    if button_backward == 1: return
    user[index] = 3
    if index == index_max:
        evaluate()
    else:
        index += 1

@onevent
def button_left():
    global user, index
    if button_left == 1: return
    user[index] = 4
    if index == index_max:
        evaluate()
    else:
        index += 1

def evaluate():
    global leds_top, motor_left_target, motor_right_target, index
    success = True
    for i in range(4):
        if code[i] != user[i]:
            success = False
    if success: # right code
        nf_sound_freq(880, 30)
        leds_top = GREEN
        motor_left_target = 150
        motor_right_target = 150
    else:       # wrong code
        leds_top = RED
        nf_sound_system(1)
