REAL_HARDWARE = True
RECORD_VIDEO = True

SERVO_PIN = 13
MOTOR_PIN = 18

CENTER_ANGLE = 162
LEFT_ANGLE = 99
RIGHT_ANGLE = 222

BASE_SPEED = 2048

if REAL_HARDWARE:
  import Encoder
  import RPi.GPIO as GPIO
  import wiringpi
  import cv2
  import numpy as np
  import VL53L1X
  import time


  Tuner = Encoder.Encoder(17, 27)

  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  wiringpi.wiringPiSetupGpio()

  wiringpi.pinMode(SERVO_PIN, wiringpi.GPIO.PWM_OUTPUT)
  wiringpi.pinMode(MOTOR_PIN, wiringpi.GPIO.PWM_OUTPUT)
  
  GPIO.setup(12, GPIO.OUT)
  pwm = GPIO.PWM(12, 50)
  
  wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
  wiringpi.pwmSetClock(192)
  wiringpi.pwmSetRange(2000)

  wiringpi.pwmWrite(SERVO_PIN, 165)

  GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

  """
  GPIO.setup(16, GPIO.OUT)
  GPIO.setup(26, GPIO.OUT)


  GPIO.output(26, 0)
  GPIO.output(16, 0)
  time.sleep(0.1)

  GPIO.output(26, 1)
  time.sleep(1)
  tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
  tof1.open()
  tof1.change_address(0x2a)
  tof1.close()

  tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x2a)
  tof1.open()

  GPIO.output(16, 1)
  time.sleep(0.1)
  tof2 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
  tof2.open()

  tof2.set_user_roi(VL53L1X.VL53L1xUserRoi(6, 9, 9, 6))
  tof1.set_user_roi(VL53L1X.VL53L1xUserRoi(6, 9, 9, 6))
  
  # tof1.set_timing(66000, 70)
  # tof2.set_timing(66000, 70)

  tof2.start_ranging(1)
  tof1.start_ranging(1)

  """
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

  def read_encoder():
    return int(Tuner.read())

  def set_direction(direction):
    if direction:
      pwm.stop()
    else:
      pwm.start(100)


  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 384)

  def set_resolution(fullhd):
    if fullhd:
      cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
      cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    else:
      cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
      cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 384)


  if RECORD_VIDEO:
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter("./video.mkv", fourcc, 20, (512, 384))



  def get_frame(show=True):
    flag, img = cap.read()

    if not flag:
      return flag, None

    if img.shape[0] != 1080:
      img =  img[:, :440]
    # cv2.imshow("pre", img)

    if show:
      cv2.imshow('img', img)

    if RECORD_VIDEO:
      out.write(img)
    

    return flag, img 



  def close_all():
    cap.release()
    if RECORD_VIDEO: out.release()
    stop_center()
    cv2.destroyAllWindows()
    exit()


  import signal
  signal.signal(signal.SIGINT, lambda signal, frame: close_all())

  def read_sensors():
    b = time.time()
    a = tof1.get_distance(),  tof2.get_distance()   
    print(time.time() - b)
    return a

  def read_button():
    return GPIO.input(26) != GPIO.HIGH

else:
  import cv2
  import time
  cap = cv2.VideoCapture(1)

  def get_frame(show=True):
    flag, img = cap.read()
    img = cv2.resize(img, (512, 384))

    if not flag:
      return flag, None

    if show: 
      cv2.imshow('img', img)

    return flag, img

  def close_all():
    cap.release()
    cv2.destroyAllWindows()

  def forward(speed=1): pass
  def stop(): pass
  def steer(angle): pass
  def stop_center(): pass
  def set_direction(direction): pass
  e = 0
  def read_encoder():
    global e
    e+=100
    time.sleep(0.1)
    return e
