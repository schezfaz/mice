from random import randint
import time
import keyboard
import threading as th
from datetime import datetime, timedelta
import pyautogui as pg

pg.FAILSAFE = False #disable: drag mouse to lhs top corner to exit script

run_script = True
def exit_code():  #press esc key to quit loop
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
        half = time_period/2
        if time_period < 300:
            upper_interval = half
        else:
            upper_interval = 299
        time_interval = randint(1, upper_interval) #dummy interval, later caliber it based on time_period
        print(time_interval)
        for i in range(time_interval):
            if run_script:
                time.sleep(1)
            else:
                print("Exiting")
                break

        time.sleep(time_interval) #time interval between each move from one position to another
        pg.moveTo(x,y)


idle_mouse(6000)
