# The Thymio relay
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# The first Thymio waits on the start line; the others wait at equal distances along the track. Write two programs so the robots carry the relay to the finish line.
#
# STEP BY STEP
# 1. Robot 1 starts when you touch its forward button, and stops when it sees the next robot in front of it.
# 2. The other robots start when their back sensors feel the previous robot arriving, and stop when they see the next robot in front.
# 3. The last robot stops on the black finish line.
# 4. Load program 1 on the first robot and program 2 on all the others.
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

speed = 100

@onevent
def prox():
    global motor_left_target, motor_right_target
    # your code here
