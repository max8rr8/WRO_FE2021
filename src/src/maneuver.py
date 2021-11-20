from config import ENABLE_MOTORS
import hardware
import time
from consts import DIRECTION_CCW, DIRECTION_CW
from src.marker import find_main_marker, is_left_marker, get_count_markers, add_count_marker

def maneuver(angle, encoder_ticks):
    last_left_seen = 0 # time.time()

    if not ENABLE_MOTORS:
        return

    hardware.steer(angle)
    start_tick = hardware.read_encoder()
    cnt = 0
    while hardware.wait_button():
        hardware.steer(angle)
        if ENABLE_MOTORS:
            hardware.forward()
        time.sleep(0.07)
        current_tick = hardware.read_encoder()
        
        #### BETA BETA BETA Unteseted
        # flag, img = hardware.get_frame()
        # marker = find_main_marker(img)


        # if angle != 0 and current_sector in [1,2,3,4] and is_left_marker(marker, DIRECTION_CW if angle > 0 else DIRECTION_CCW):
        #     print("SEEN LEFT MANEUVER", time.time() - last_left_seen)
        #     if time.time() - last_left_seen > 2:
        #         add_count_marker()
        #         print("DETECTED LEFT MARKER", get_count_markers(), time.time() - last_left_seen)

        #     last_left_seen = time.time()

        # find_main_marker(img)
        
        if abs(current_tick - start_tick) > encoder_ticks:
            hardware.get_frame()
            break

def complex_maneuver(forward, angle, encoder_ticks):
    if forward > 0:
        maneuver(0, forward)
    maneuver(angle, encoder_ticks)

    # hardware.stop_center()
    # time.sleep(100000)