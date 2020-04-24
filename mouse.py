from random import randint
import time
from datetime import datetime, timedelta
import pyautogui as pg

pg.FAILSAFE = True #drag mouse to lhs top corner to exit script

def idle_mouse(time_period, time_interval):
    width, height = pg.size()  #get screen resolution
    print(width,height)

    end_time = datetime.now() + timedelta(seconds=time_period)
    while datetime.now() < end_time:
        current_position = pg.position()  # get current location of mouse
        print(current_position)
        x, y = randint(0, width - 1), randint(0, height - 1)
        time.sleep(time_interval) #time interval between each move from one position to another
        pg.moveTo(x,y)

idle_mouse(5,1)