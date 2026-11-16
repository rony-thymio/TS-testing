# Keep on track
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Thymio follows a black line back and forth, a little faster each time, without "derailing".
#
# STEP BY STEP
# 1. Both ground sensors on black: go straight (blue light).
# 2. Only the left sensor on black: turn left (green light).
# 3. Only the right sensor on black: turn right (yellow light).
# 4. Both sensors on white: the end of the line is reached, make a U-turn (red light) and speed up by 1.
# 5. How long does Thymio last before it leaves the line?
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

speed = 150
gap = 1

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top, speed
    # your code here
