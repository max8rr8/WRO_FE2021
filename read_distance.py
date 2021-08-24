import hardware
import time

while True:
    print(hardware.read_sensors())
    time.sleep(1)