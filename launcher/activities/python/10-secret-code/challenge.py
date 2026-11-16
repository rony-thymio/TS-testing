# Secret start code
# Joël Rivet, "Programmer Thymio avec Python et Thonny" (CC BY-NC), adapted into English
#
# YOUR GOAL
# Thymio only starts after the right sequence of 4 button presses. The same button can be used several times.
#
# STEP BY STEP
# 1. Give each button a number: 0 centre, 1 forward, 2 right, 3 backward, 4 left.
# 2. Store the secret code in a list, and the buttons typed in another list.
# 3. After the 4th press, compare the two lists.
# 4. Right code: green light, a short high note, and Thymio drives off.
# 5. Wrong code: red light and system sound 1 (the "switch off" sound).
#
# Run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? The challenge window shows hints, one at a time.

code = [1, 2, 2, 0] # the secret code, choose your own
user = [-1] * 6
index = 0

@onevent
def button_forward():
    global user, index
    # your code here
