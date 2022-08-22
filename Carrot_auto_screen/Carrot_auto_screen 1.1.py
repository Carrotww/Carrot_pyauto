import pyautogui
import time
import random
import sys
import psutil
import tkinter as tk
import threading

def th():
    print('start')
    while True:
        pyautogui.FAILSAFE = True
        screenW, screenH = pyautogui.size()
        temp_x, temp_y = pyautogui.position()
        time.sleep(145)
        current_x, current_y = pyautogui.position()

        if temp_x == current_x and temp_y == current_y:
            ran_w = random.randint(1, screenW)
            ran_h = random.randint(1, screenH)

            pyautogui.moveTo(ran_w, ran_h, 0.3)
            pyautogui.typewrite(" ", 1)
            # print(temp_x, temp_y)
            # print(current_x, current_y)

start = threading.Thread(target=th)

def button_start():
    global start
    start.start()

def button_stop():
    global start
    start.stop()
    print('system stop')

def button_shutdown():
    print('system halt')
    sys.exit(0)

win = tk.Tk()
win.title('hyeongseok auto screen')
tk.Button(win, text='start', width=50, height=3, command=button_start()).grid(column=0, row=1, columnspan=4)
tk.Button(win, text='stop', width=50, height=3, command=button_stop()).grid(column=0, row=2, columnspan=4)
tk.Button(win, text='shutdown', width=50, height=3, command=button_shutdown()).grid(column=0, row=3, columnspan=4)
win.mainloop()

# for proc in psutil.process_iter():
#     ps_name = proc.name()
#     cmdline = proc.cmdline()
#
# for proc in psutil.process_iter():
#   ps_name = proc.name()
#   if ps_name == 'python3':
#     cmdline = proc.cmdline()
#     print(cmdline)