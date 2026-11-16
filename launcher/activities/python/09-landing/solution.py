# Solution: Landing
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
delta = 0
color = 0
height = 0
contact = 0
threshold = 4 # so that the red does not light up too early

@onevent
def prox():
    global delta, color, height, contact
    if contact == 0:
        delta = (prox_ground_delta[0] + prox_ground_delta[1]) // 2
        if delta > threshold:
            color = delta // 30 + 7
            nf_leds_top(color, 0, 0)
        height = 440 + delta
        nf_sound_freq(height, 10)

@onevent
def tap():
    global contact, leds_top
    contact = 1
    leds_top = [0, 32, 0]
    nf_sound_freq(55, 150)
