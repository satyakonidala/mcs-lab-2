import picar_4wd as fc
import time
import numpy as np
import math
import RPi.GPIO as GPIO
import json

def mforward():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.forward(15)
    x = 0
    for i in range(3):
        time.sleep(0.1)

    speed4.deinit()
    fc.stop()

def mbackward():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.backward(15)
    x = 0
    for i in range(3):
        time.sleep(0.1)

    speed4.deinit()
    fc.stop()

def mleft():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.turn_left(15)
    x = 0
    for i in range(3):
        time.sleep(0.1)
    speed4.deinit()
    fc.stop()



def mright():
    speed4 = fc.Speed(25)
    speed4.start()
    fc.turn_right(15)
    x = 0
    for i in range(3):
        time.sleep(0.1)
    speed4.deinit()
    fc.stop()

def car_state():
    state = fc.utils.pi_read()
    return json.dumps(state)
