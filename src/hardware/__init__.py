
from config.hardware import *
import Encoder
import RPi.GPIO as GPIO
import wiringpi
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
wiringpi.wiringPiSetupGpio()

from hardware.button import *
from hardware.led import *

def wait_for_start():
    while not read_button():
        led(1,1,1)
        time.sleep(0.1)
    led(0,0,0)

if DO_WAIT:
    wait_for_start()
        

        
    

from hardware.camera import *
from hardware.distance import *
from hardware.encoder import *
from hardware.movement import *

def close_all():
    print("EXITING")
    cap.release()
    stop_center()
    cv2.destroyAllWindows()
    led(0,0,0)
    exit()

import signal
signal.signal(signal.SIGINT, lambda signal, frame: close_all())

import atexit
atexit.register(lambda: close_all())
