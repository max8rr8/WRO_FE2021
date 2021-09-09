from src.rotate import should_start_rotate
from src.maneuver import complex_maneuver
from config.maneuver import MANEUVERS
from src.wall import wall
from config.config import POINT_SHIFT
from src.marker import find_main_marker, find_side_markers, get_last_marker
from src.direction import find_direction, recognize_direction
import cv2
import numpy as np
import time
import hardware
from config import ENABLE_MOTORS

######################################################################################
######################################################################################
######################################################################################

hardware.set_resolution(True)
direction = find_direction()
hardware.set_resolution(False)

hardware.reset_encoder()
for i in range(7):
    hardware.get_frame()
    cv2.waitKey(1)

current_sector = 0

start_ticks = hardware.read_encoder()
final_sector_ticks = 0

while True:
    start_time = time.time()
    flag, img = hardware.get_frame()

    marker = find_main_marker(img)
    point_shift = POINT_SHIFT[marker]

    wall(img, direction, POINT_SHIFT[marker])

    if ENABLE_MOTORS:
        hardware.forward()

    if current_sector == 12 and hardware.read_encoder() > til_finish_ticks:
        hardware.stop_center()
        exit()

    if should_start_rotate(img):
        if current_sector == 0:
            til_finish_ticks = hardware.read_encoder()
        elif current_sector == 4 or current_sector == 8:
            final_sector_ticks += hardware.read_encoder()
        elif current_sector == 11:
            til_finish_ticks = final_sector_ticks / 2 - til_finish_ticks

        last_marker = get_last_marker()
        current_marker = find_side_markers(img, direction)

        complex_maneuver(MANEUVERS[direction][last_marker][current_marker])

        current_sector += 1
        hardware.reset_encoder()

    ch = cv2.waitKey(5)
    if ch == 27:
        break

    if hardware.read_button():
        exit()
