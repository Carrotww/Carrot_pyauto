import pyautogui
import time
import random

while True:
    pyautogui.FAILSAFE = True
    screenW, screenH = pyautogui.size()
    ran_w = random.randint(1, screenW)
    ran_h = random.randint(1, screenH)

    pyautogui.moveTo(ran_w, ran_h, 0.3)
    pyautogui.typewrite(" ", 1)
    time.sleep(250)