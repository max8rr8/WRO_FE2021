from config.hardware import LED_PINS
import RPi.GPIO as GPIO

for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)


def led(r, g, b):
    GPIO.output(pin[0], GPIO.HIGH if r else GPIO.LOW)
    GPIO.output(pin[1], GPIO.HIGH if g else GPIO.LOW)
    GPIO.output(pin[2], GPIO.HIGH if b else GPIO.LOW)