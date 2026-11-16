# Timid Thymio
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Recreate the red "scared" behaviour that is built into Thymio, with your own Python program.
#
# STEP BY STEP
# 1. If Thymio sees nothing around it, it stays still.
# 2. If something appears at the front left, Thymio backs away while turning to the right. At the front right, it backs away turning to the left.
# 3. If something appears at the back left, Thymio moves forward while turning to the right. At the back right, it moves forward turning to the left.
# 4. If something is right in front of it, Thymio backs straight away.
# 5. If Thymio is surrounded (front and back), it stops, lights up red and plays system sound 4.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top
    # your code here
