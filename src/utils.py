import hardware
import time

def report_start():
    hardware.steer(-50)
    time.sleep(0.5)
    hardware.steer(50)
    time.sleep(0.5)
    hardware.stop_center()
