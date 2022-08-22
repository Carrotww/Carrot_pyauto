import pyautogui
import time
import random
import sys
import psutil
import tkinter as tk

status = 1

def button_start(val):
    print("start")
    global status
    status = 1

    while True:
        pyautogui.FAILSAFE = True
        screenW, screenH = pyautogui.size()
        temp_x, temp_y = pyautogui.position()
        if status == False:
            break
        time.sleep(145)
        current_x, current_y = pyautogui.position()
        if temp_x == current_x and temp_y == current_y:
            ran_w = random.randint(1, screenW)
            ran_h = random.randint(1, screenH)

            pyautogui.moveTo(ran_w, ran_h, 0.3)
            pyautogui.typewrite(" ", 1)
            # print(temp_x, temp_y)
            # print(current_x, current_y)

def button_stop(val):
    global status
    print('system stop')
    status = 0
    return status

def button_shutdown(val):
    global status
    print('system halt')
    status = 0
    time.sleep(4)
    sys.exit(0)

win = tk.Tk()
win.title('hyeongseok auto screen')
tk.Button(win, text = 'start', width=50, height=3, command= lambda cmd=status: button_start(cmd)).grid(column=0, row=1, columnspan=4)
tk.Button(win, text = 'stop', width=50, height=3, command= lambda cmd=status: button_start(cmd)).grid(column=0, row=2, columnspan=4)
tk.Button(win, text = 'shutdonw', width=50, height=3, command= lambda cmd=status: button_start(cmd)).grid(column=0, row=3, columnspan=4)
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