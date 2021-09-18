
from hardware.consts import *
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

def close_all():
    cap.release()
    stop_center()
    cv2.destroyAllWindows()
    exit()

import signal
signal.signal(signal.SIGINT, lambda signal, frame: close_all())

import atexit
atexit.register(lambda: close_all())
