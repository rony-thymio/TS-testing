# Landing
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Hold Thymio flat about 50 cm above the table and lower it slowly. The closer it gets, the redder and the higher-pitched it becomes. When it touches the table, it turns green and plays a low note for 2 seconds.
#
# STEP BY STEP
# 1. During the descent, read the ground sensors: the closer the table, the larger prox_ground_delta.
# 2. Turn that value into a red intensity (0 to 32) and into a note that gets higher (start from 440 Hz, the A).
# 3. Touching down is the tap event: switch to green and play a low note for 2 seconds.
# 4. After landing, the approach phase must stop: use a variable for the two phases.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

contact = 0

@onevent
def prox():
    global contact
    # your code here

@onevent
def tap():
    global contact, leds_top
    # your code here
