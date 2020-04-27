from random import randint
import time
import keyboard
import threading as th
from datetime import datetime, timedelta
import pyautogui as pg

pg.FAILSAFE = True #drag mouse to lhs top corner to exit script

run_script = True
def exit_code():
    global run_script
    key_pressed = keyboard.read_key()
    if key_pressed == "esc":
        print("Exiting code")
        run_script = False

def idle_mouse(time_period):
    th.Thread(target=exit_code, args=(), name='exit_code', daemon=True).start()
    width, height = pg.size()  #get screen resolution
    print(width,height)
    end_time = datetime.now() + timedelta(seconds=time_period)
    while run_script and datetime.now() < end_time:
        current_position = pg.position()  # get current location of mouse
        print(current_position)
        x, y = randint(0, width - 1), randint(0, height - 1)
        time_interval = randint(1, 10) #dummy interval, later caliber it based on time_period
        time.sleep(time_interval) #time interval between each move from one position to another
        pg.moveTo(x,y)

idle_mouse(10)