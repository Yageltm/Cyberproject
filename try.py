import pyautogui
import time
while True:
    if pyautogui.mouseDown:
        print('down')
    elif pyautogui.mouseUp:
        print('up')
    else:
        print('bew')
