from config.config import QUALIFICATION_MODE
from config.hardware import *
import RPi.GPIO as GPIO
import wiringpi
import time

wiringpi.pinMode(SERVO_PIN, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pinMode(MOTOR_PIN, wiringpi.GPIO.PWM_OUTPUT)

GPIO.setup(16, GPIO.OUT)
# GPIO.output(16, 0)
pwm = GPIO.PWM(16, 50)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

wiringpi.pwmWrite(SERVO_PIN, 165)


def forward(speed=1):
    base_speed = QUALIFICATION_SPEED if QUALIFICATION_MODE else BASE_SPEED
    wiringpi.pwmWrite(MOTOR_PIN, int(base_speed * speed))


def stop():
    wiringpi.pwmWrite(MOTOR_PIN, 0)


def steer(angle):
    # print(angle)
    angle += CENTER_ANGLE

    # if angle < LEFT_ANGLE:
    #     angle = LEFT_ANGLE

    # if angle >= RIGHT_ANGLE:
    #     angle = RIGHT_ANGLE

    wiringpi.pwmWrite(SERVO_PIN, int(angle))


def stop_center():
    stop()
    steer(0)


def set_direction(direction):
    # pass
    if direction:
        pwm.stop()
    else:
        pwm.start(100)

def pause_for(seconds):
    stop_center()
    time.sleep(seconds)