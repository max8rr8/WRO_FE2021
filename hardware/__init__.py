
from config.hardware import *
import Encoder
import RPi.GPIO as GPIO
import wiringpi

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
wiringpi.wiringPiSetupGpio()


from hardware.camera import *
from hardware.distance import *
from hardware.encoder import *
from hardware.movement import *
from hardware.button import *
from hardware.led import *

def close_all():
    cap.release()
    stop_center()
    cv2.destroyAllWindows()
    led(0,0,0)
    exit()

import signal
signal.signal(signal.SIGINT, lambda signal, frame: close_all())

import atexit
atexit.register(lambda: close_all())
