import time
import hardware
import cv2
from consts import *
from config import OBJECTS
from src.detection import detect_object


def detect_side_markers(img, direction):
    zone = OBJECTS.SIDE_ZONE[direction]

    red_marker = detect_object(name="red_marker",
                               img=img,
                               zone=zone,
                               **OBJECTS.SIDE_RED)

    green_marker = detect_object(name="green_marker",
                                 img=img,
                                 zone=zone,
                                 **OBJECTS.SIDE_GREEN)

    return red_marker, green_marker


def find_side_markers(img, direction):
    current_marker_none = 0
    current_marker_red = 0
    current_marker_green = 0

    for i in range(3):
        flag, img = hardware.get_frame()
        side_red, side_green = detect_side_markers(img, direction)

        print("SIDE OBJECTS", side_red[1], side_green[1])
        if side_red[0] is not None:
            current_marker_red += 1
        elif side_green[0] is not None:
            current_marker_green += 1
        else:
            current_marker_none += 1
        cv2.waitKey(50)

    ma = max(current_marker_none, current_marker_red, current_marker_green)
    if ma == current_marker_red:
        return MARKER_RED
    elif ma == current_marker_green:
        return MARKER_GREEN
    else:
        return MARKER_NONE


def detect_main_markers(img):
    red_marker = detect_object(name="red_marker",
                               img=img,
                               *OBJECTS.MARKER_RED)

    green_marker = detect_object(name="green_marker",
                                 img=img,
                                 *OBJECTS.MARKER_GREEN)

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

def get_last_marker():
    if time.time() - last_marker_seen > 1:
        return MARKER_NONE
    