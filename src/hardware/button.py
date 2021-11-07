import RPi.GPIO as GPIO
import cv2

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def read_button():
    return GPIO.input(26) != GPIO.HIGH


def wait_button(cv_button=27):
    if cv2.waitKey(5) & 0xFF == cv_button:
        return False

    return not read_button()
