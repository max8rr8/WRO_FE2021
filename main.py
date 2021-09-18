import cv2
import time
import hardware
from src.rotate import should_start_rotate
from src.maneuver import complex_maneuver
from src.wall import capture_wall, wall
from src.marker import find_main_marker, find_side_markers, get_last_marker, get_side_markers
from src.direction import find_direction #, recognize_direction
from src.utils import report_start
from config import ENABLE_MOTORS, MANEUVERS
from config import POINT_SHIFT, QUALIFICATION_MODE, WALL_POINT

######################################################################################
######################################################################################
######################################################################################

hardware.set_resolution(True)
report_start()
direction = find_direction()
hardware.set_resolution(False)

hardware.reset_encoder()
for i in range(7):
    hardware.get_frame()
    cv2.waitKey(1)

start_wall_point = capture_wall(direction)
current_sector = 0

start_ticks = hardware.read_encoder()
final_sector_ticks = 0
print("AA")
while True:
    start_time = time.time()
    flag, img = hardware.get_frame()

    if QUALIFICATION_MODE:
        wall(img, direction,
             start_wall_point if current_sector % 4 == 0 else WALL_POINT)
    else:
        marker = find_main_marker(img)
        point_shift = POINT_SHIFT[marker]

        wall(img, direction, POINT_SHIFT[marker])

        find_side_markers(img)

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
        side_marker = get_side_markers()
        
        print("Eexecuting maneuver", direction, last_marker, side_marker)
        complex_maneuver(*MANEUVERS[direction][last_marker][side_marker])

        current_sector += 1
        hardware.reset_encoder()

        img = None

    ch = cv2.waitKey(5)
    if ch == 27:
        break

    if hardware.read_button():
        exit()
