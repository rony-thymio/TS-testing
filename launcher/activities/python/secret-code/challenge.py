# Secret start code
# Activity by Joël Rivet (licence CC BY-NC), from "Programmer Thymio avec Python et Thonny", session 1.
# English adaptation for Thymio Suite.
#
# THE CHALLENGE
# Write a program that lets Thymio start only if you type a password.
# The password is a sequence of 4 button presses among the 5 buttons
# (the centre button and the 4 arrows); the same button can be used several
# times. After the 4th press:
# - if the code is right, Thymio starts in green with a short high note;
# - if the code is wrong, Thymio turns red with system sound 1.
# Each button has a number:
# 0 centre, 1 forward, 2 right, 3 backward, 4 left.
# Note: if you store the codes in lists, Aseba cannot compare two lists with
# a single ==: compare them element by element in a loop.
#
# To run it: Thymio > Run on Thymio (Ctrl+Shift+R). Stop: Thymio > Stop Thymio.
# Stuck? Click "Hints" on the activity in Thymio Suite.

code = [1, 2, 2, 0] # the secret code, choose your own

@onevent
def button_center():
    global leds_top
    # your code here
    pass
