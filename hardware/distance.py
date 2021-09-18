import VL53L1X
import time
"""
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)


GPIO.output(26, 0)
GPIO.output(16, 0)
time.sleep(0.1)

GPIO.output(26, 1)
time.sleep(1)

time.sleep(0.5)
tof1 = VL53L1X.VL53L1X(i2c_bus=1, i2c_address=0x29)
time.sleep(0.5)

tof1.open()

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


def read_distance():
    # b = time.time()
    # a = tof1.get_distance()
    return tof1.get_distance()