import pyautogui

while True:
    if not pyautogui.mouseDown(button='left'):
        x, y = pyautogui.position()
        print(f"Mouse position: x={x}, y={y}")
jects/MouseProject/get_coor.py
