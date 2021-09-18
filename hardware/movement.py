from hardware.consts import *
import RPi.GPIO as GPIO
import wiringpi
import time

wiringpi.pinMode(SERVO_PIN, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(MOTOR_PIN, wiringpi.GPIO.PWM_OUTPUT)

GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

wiringpi.pwmWrite(SERVO_PIN, 165)


def forward(speed=1):
    wiringpi.pwmWrite(MOTOR_PIN, int(BASE_SPEED * speed))


def stop():
    wiringpi.pwmWrite(MOTOR_PIN, 0)


def steer(angle):
    angle += CENTER_ANGLE

    if angle < LEFT_ANGLE:
        angle = LEFT_ANGLE

    if angle >= RIGHT_ANGLE:
        angle = RIGHT_ANGLE

    wiringpi.pwmWrite(SERVO_PIN, int(angle))


def stop_center():
    stop()
    steer(0)


def set_direction(direction):
    if direction:
        pwm.stop()
    else:
        pwm.start(100)

def pause_for(seconds):
    stop_center()
    time.sleep(seconds)