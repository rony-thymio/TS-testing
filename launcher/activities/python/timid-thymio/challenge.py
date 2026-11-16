# Timid Thymio
# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
#
# THE CHALLENGE
# Maybe you know the red pre-programmed behaviour, the "scared" Thymio.
# Program the same behaviour yourself:
# - If Thymio sees nothing around it, it stays still.
# - If something appears at the front left (front right), Thymio moves back
#   while turning to the right (to the left).
# - If something appears at the back left (back right), Thymio moves forward
#   while turning to the right (to the left).
# - If Thymio is surrounded, it stops, lights up red and plays system sound 4.
# To keep the number of cases small, you can ignore front sensors 1 and 3.
#
# To run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? Click "Hints" on the activity in Thymio Suite.

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top
    # your code here
    pass
