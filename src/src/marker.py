import time
import hardware
import cv2
from consts import *
from config import OBJECTS
from src.detection import detect_object


def detect_side_markers(img, direction):
    if direction == DIRECTION_CW:
        red_marker = detect_object(name="side_red_marker",
                               img=img,
                               **OBJECTS.SIDE_RED)
        return red_marker, (None, None)
    else:
        green_marker = detect_object(name="side_green_marker",
                                 img=img,
                                 **OBJECTS.SIDE_GREEN)

        return (None, None), green_marker

side_markers_memory = []

i = 0

def find_side_markers(img, direction):
    global side_markers_memory
    global i
    flag, img = hardware.get_frame()
    cv2.imwrite(f"t{i}.png", img)
    i=(i+1)%7
    # print(i)
    side_markers_memory.append(detect_side_markers(img, direction))
    side_markers_memory = side_markers_memory[-7:]
        
def get_side_markers():
    # return MARKER_RED

    current_marker_none = 0
    current_marker_red = 0
    current_marker_green = 0

    for side_red, side_green in side_markers_memory:
        print("SIDE OBJECTS", side_red[1], side_green[1])
    

    for side_red, side_green in side_markers_memory[:5]:
        if side_red[0] is not None:
            current_marker_red += 1
        elif side_green[0] is not None:
            current_marker_green += 1
        else:
            current_marker_none += 1

    ma = max(current_marker_none, current_marker_red, current_marker_green)
    print(ma, current_marker_green, current_marker_green, current_marker_none)
    if ma == current_marker_red:
        return MARKER_RED
    elif ma == current_marker_green:
        return MARKER_GREEN
    else:
        return MARKER_NONE


def detect_main_markers(img):
    red_marker = detect_object(name="red_marker",
                               img=img,
                               **OBJECTS.RED_MARKER)

    green_marker = detect_object(name="green_marker",
                                 img=img,
                                 **OBJECTS.GREEN_MARKER)

    return red_marker, green_marker


last_marker = MARKER_NONE
last_marker_seen = time.time()

def find_main_marker(img): 
    global last_marker
    global last_marker_seen


    red_marker, green_marker = detect_main_markers(img)
    marker = MARKER_NONE
    if red_marker[0] is not None:
        marker = MARKER_RED
    elif green_marker[0] is not None:
        marker = MARKER_GREEN
    
    if marker != MARKER_NONE:
        last_marker = marker
        last_marker_seen = time.time()

    ## BETA BETA BETA BETA untested
    # if marker == MARKER_NONE and (time.time() - last_marker_seen) < 1:
    #     marker = last_marker

    return marker

def is_left_marker(marker, direction):
    # if direction == DIRECTION_CW and marker == MARKER_GREEN:
    #     return True
    if marker == MARKER_RED:
        return True
    return False

def get_last_marker():
    if time.time() - last_marker_seen > 1:
        return MARKER_NONE
    return last_marker 

def led_marker(marker):
    if marker == MARKER_RED:
        hardware.led(1,0,0)
    elif marker == MARKER_GREEN:
        hardware.led(0,1,0)
    else:
        hardware.led(0,0,1)


count_of_markers = 0
def add_count_marker():
    global count_of_markers
    count_of_markers += 1

def get_count_markers():
    return count_of_markers