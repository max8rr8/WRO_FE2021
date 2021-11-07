import cv2
import numpy as np
from config import WALL_SEARCH_Y, KP, KD
from config import WALL_BIN, WALL_POINT, WALL_SEARCH_X
from src.detection import binarize
from consts import *
import hardware


def find_wall(img, direction):
    img = img[WALL_SEARCH_Y[0]:WALL_SEARCH_Y[1]]
    if direction == DIRECTION_CW:
        img = img[:, :WALL_SEARCH_X]
    else:
        img = img[:, -WALL_SEARCH_X:]

    cv2.imshow("ROAD", img)
    binarized = binarize(img=img, **WALL_BIN)

    debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)

    # For each row calculate last white pixel, and then get average of them
    lowest_points = np.argmax(binarized[::-1], axis=0)
    lowest_point = binarized.shape[0] - np.average(lowest_points)

    cv2.line(debug, (0, int(lowest_point)), (80, int(lowest_point)),
             (0, 255, 0), 2)
    cv2.imshow("Wall", debug)

    return lowest_point


errold = 0


def calculate_point(direction, base_point, delta_point):
    if direction == DIRECTION_CW:
        return base_point + delta_point
    else:
        return base_point - delta_point


def wall(img, direction, target_point):
    """
    Езда по стене
    img - картинка
    direction - направление езды
    target_point - точка по которой нужно держаться стены
    """

    current_point = find_wall(img, direction)
    # print("Current_pont",current_point)
    err = current_point - target_point

    global errold
    u = KP * err + KD * (err - errold)
    errold = err

    # print("PID U U U U Uu U", u)
    if u < -48:
        u = -48
    elif u > 48:
        u = 48

    if direction == DIRECTION_CCW:
        u = -u

    hardware.steer(u)


def capture_wall(direction):
    point = 0
    for i in range(5):
        flag, img = hardware.get_frame()
        point += find_wall(img, direction)
        cv2.waitKey(10)
    return point / 5