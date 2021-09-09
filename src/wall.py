import cv2
import numpy as np
from config import ROAD_SEARCH_Y, KP, KD
from config import CW_POINT, CCW_POINT, WALL_BIN
from src.detection import binarize
from consts import *
import hardware


def find_wall(img, direction):
    img = img[ROAD_SEARCH_Y[0]:ROAD_SEARCH_Y[1]]
    if direction == DIRECTION_CW:
        img = img[:, :80]
    else:
        img = img[:, -80:]

    cv2.imshow("ROAD", img)
    binarized = binarize(img=img, **WALL_BIN)

    debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)

    lowest_points = np.argmax(binarized[::-1], axis=0)
    lowest_point = binarized.shape[0] - np.average(lowest_points)

    cv2.line(debug, (0, int(lowest_point)), (80, int(lowest_point)),
             (0, 255, 0), 2)
    cv2.imshow("Wall", debug)

    return lowest_point


errold = 0


def wall(img, direction, delta_point):
    """
    Езда по стене
    img - картинка
    direction - направление езды
    delta_point - изменение относительно основной точки
    """

    if direction == DIRECTION_CW:
        target_point = CW_POINT + delta_point
    else:
        target_point = CCW_POINT - delta_point

    current_point = find_wall(img, direction)
    err = current_point - target_point

    global errold
    u = KP * err + KD * (err - errold)
    errold = err

    if direction == DIRECTION_CCW:
        u = -u

    hardware.steer(u if direction else -u)

def capture_wall(direction):
    point = 0
    for i in range(5):
        flag, img = hardware.get_frame()
        point += find_wall(img, direction)
        cv2.waitKey(10)
    return point / 5