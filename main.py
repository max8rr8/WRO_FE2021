from config.maneuver import QUALIFICATION_PRE_FINAL_MANEUVER
import cv2
import time
import hardware
from src.rotate import should_start_rotate
from src.maneuver import complex_maneuver
from src.wall import capture_wall, wall, calculate_point
from src.marker import find_main_marker, find_side_markers, get_last_marker, get_side_markers, led_marker
from src.direction import find_direction  #, recognize_direction
from src.utils import report_start
from config import ENABLE_MOTORS, MANEUVERS, QUALIFICATION_SECTOR_BORDERS
from config import POINT_SHIFT, QUALIFICATION_MODE, WALL_POINT
from config import QUALIFICATION_WALL_POINT, QUALIFICATION_MANEUVER

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
    cv2.waitKey(10)

start_wall_point = capture_wall(direction)
current_sector = 0

start_ticks = hardware.read_encoder()
final_sector_ticks = 0
print("Direction:", direction, " Mode:", QUALIFICATION_MODE)
while hardware.wait_button():
    start_time = time.time()
    flag, img = hardware.get_frame()

    if QUALIFICATION_MODE:
        hardware.led(0, 0, 1)
        wall(
            img, direction, start_wall_point if current_sector %
            4 == 0 else QUALIFICATION_WALL_POINT)

    else:
        marker = find_main_marker(img)
        led_marker(marker)
        point_shift = POINT_SHIFT[marker]
        point = calculate_point(direction, WALL_POINT, point_shift)
        print(marker, point)
        wall(img, direction, point)

        find_side_markers(img, direction)

    if ENABLE_MOTORS:
        hardware.forward()

    if current_sector == 12 and hardware.read_encoder() > til_finish_ticks:
        hardware.stop_center()
        exit()

    if should_start_rotate(img):
        hardware.led(1, 1, 1)

        if current_sector == 0:
            til_finish_ticks = hardware.read_encoder()
        elif current_sector == 4 or current_sector == 8:
            final_sector_ticks += hardware.read_encoder()
        elif current_sector == 11:
            til_finish_ticks = final_sector_ticks / 2 - til_finish_ticks - 100

        if QUALIFICATION_MODE:
            if current_sector % 4 == 3:
                if start_wall_point > QUALIFICATION_SECTOR_BORDERS[1]:
                    side_sector = -1
                elif start_wall_point < QUALIFICATION_SECTOR_BORDERS[0]:
                    side_sector = +1
                else:
                    side_sector = 0

                print("Executing qualification pre-final maneuver", direction, side_sector)

                complex_maneuver(*QUALIFICATION_PRE_FINAL_MANEUVER[direction][side_sector])
            else:
                print("Executing qualification base maneuver", direction)
                complex_maneuver(*QUALIFICATION_MANEUVER[direction])
        else:
            last_marker = get_last_marker()
            side_marker = get_side_markers()

            print("Executing maneuver", direction, last_marker, side_marker)
            complex_maneuver(*MANEUVERS[direction][last_marker][side_marker])

        current_sector += 1
        hardware.reset_encoder()

        img = None

        for i in range(5):
            a = hardware.get_frame()
            cv2.waitKey(10)
