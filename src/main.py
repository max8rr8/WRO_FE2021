from config.maneuver import QUALIFICATION_PRE_FINAL_MANEUVER
import cv2
import time
import hardware
from src.rotate import should_start_rotate
from src.maneuver import complex_maneuver
from src.wall import capture_wall, wall, calculate_point
from src.marker import get_count_markers, add_count_marker, is_left_marker, find_main_marker, find_side_markers, get_last_marker, get_side_markers, led_marker
from src.direction import find_direction  #, recognize_direction
from src.utils import report_start
from config import ENABLE_MOTORS, MANEUVERS, QUALIFICATION_SECTOR_BORDERS
from config import POINT_SHIFT, QUALIFICATION_MODE, WALL_POINT
from config import QUALIFICATION_WALL_POINT, QUALIFICATION_MANEUVER
from consts import MARKER_RED

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
print(start_wall_point)

current_sector = 0

start_ticks = hardware.read_encoder()
final_sector_ticks = 0
print("Direction:", direction, " Mode:", QUALIFICATION_MODE)

if ENABLE_MOTORS:
    hardware.forward(10)
    time.sleep(0.2)

last_left_seen = 0
count_of_markers = 0

final_sector = 11

roro = 0

while hardware.wait_button():
    start_time = time.time()
    flag, img = hardware.get_frame()
    # print(img.shape)

    if QUALIFICATION_MODE:
        hardware.led(0, 0, 1)
        wall(
            img, direction, (start_wall_point + 15) if current_sector == 0 else QUALIFICATION_WALL_POINT)

    else:
        marker = find_main_marker(img)


        if current_sector in [1,2,3,4] and is_left_marker(marker, direction):
            # print("SEEN", time.time() - last_left_seen)
            if time.time() - last_left_seen > 0.8:
                add_count_marker()

                cv2.imwrite(f"red{roro}.png", img)
                roro+=1
                print("DETECTED LEFT MARKER", get_count_markers(), time.time() - last_left_seen)

            last_left_seen = time.time()

        led_marker(marker)
        point_shift = POINT_SHIFT[marker]
        point = calculate_point(direction, start_wall_point if current_sector == 12 else WALL_POINT[direction], point_shift)
        # print("Marker", marker)
        wall(img, direction, point)

        find_side_markers(img, direction)

    if ENABLE_MOTORS:
        hardware.forward()

    if current_sector == final_sector + 1 and hardware.read_encoder() > til_finish_ticks:

        print("FINAL SECTORS", get_count_markers(), final_sector)
        hardware.stop_center()
        exit()

    if should_start_rotate(img, direction):
        hardware.led(1, 1, 1)

        if current_sector == 0:
            til_finish_ticks = hardware.read_encoder()
        elif current_sector == 4 or current_sector == 8:
            print("FINAL SECTOR TOOK", hardware.read_encoder())
            final_sector_ticks += hardware.read_encoder()
        elif current_sector == 7:
            print("FINAL SECTOR", get_count_markers())
            # final_sector += get_count_markers()
        elif current_sector == final_sector:
            print("FINAL SECTORS", get_count_markers())
            til_finish_ticks = 1100 # final_sector_ticks / 2 - til_finish_ticks - 260

        if QUALIFICATION_MODE:
            # if current_sector % 4 == 3:
            #     if start_wall_point > QUALIFICATION_SECTOR_BORDERS[1]:
            #         side_sector = -1
            #     elif start_wall_point < QUALIFICATION_SECTOR_BORDERS[0]:
            #         side_sector = +1
            #     else:
            #         side_sector = 0

            #     print("Executing qualification pre-final maneuver", direction, side_sector)

            #     complex_maneuver(*QUALIFICATION_PRE_FINAL_MANEUVER[direction][side_sector])
            # else:
            print("Executing qualification base maneuver", direction)
            complex_maneuver(*QUALIFICATION_MANEUVER[direction])
        else:
            last_marker = get_last_marker()
            side_marker = get_side_markers()


            print("Executing maneuver", direction, last_marker, side_marker)
            complex_maneuver(*MANEUVERS[direction][last_marker][side_marker])
            # hardware.stop_center()
            # exit()
            if side_marker == MARKER_RED:
                last_left_seen = time.time()

            if current_sector in [1,2,3,4] and side_marker == MARKER_RED:
                add_count_marker()
                flag, img = hardware.get_frame()
                cv2.imwrite(f"red{roro}.png", img)
                roro+=1

        current_sector += 1
        hardware.reset_encoder()

        img = None

        for i in range(10):
            a = hardware.get_frame()
            cv2.waitKey(1)
        # last_left_seen = time.time()
        # if current_sector == 1:
        #     exit(1)
    