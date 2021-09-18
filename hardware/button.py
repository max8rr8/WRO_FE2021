
import RPi.GPIO as GPIO

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def read_button():
    return GPIO.input(26) != GPIO.HIGH