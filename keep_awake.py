import pyautogui
import time


sleep_time_in_seconds = 150 # 2.5 min 
# find the current mouse position and move it one in x, and y Then sleep for 2.5 min 
while(True):
    current_position = pyautogui.position()
    x = current_position.x + 1
    y = current_position.y + 1 
    pyautogui.moveTo(x, y)
    print("mouse has been moved")
    time.sleep(sleep_time_in_seconds)
   

