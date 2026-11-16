# Thymio the explorer
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Thymio drives around the table, avoids each obstacle by going around it on the left or on the right, and stops at the edge of the table.
#
# STEP BY STEP
# 1. Thymio waits. When you touch the forward button, it starts driving. The centre button stops it.
# 2. While driving, compare what the left sensors and the right sensors see: turn away from the side that sees more.
# 3. If something is right in front, turn anyway.
# 4. If a ground sensor sees nothing below it (the edge of the table), stop for good.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

stop = True
speed = 150

@onevent
def button_forward():
    global stop
    # your code here

@onevent
def prox():
    global motor_left_target, motor_right_target, leds_top
    if stop: return
    # your code here
