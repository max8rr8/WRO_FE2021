import cv2
import numpy as np
import math
import time
import hardware
import atexit

KP = 0.7
KD = 0.5
ROUNDER = 1000
DISTANCE = 500

LEFT90_MANEUVER = (-40,  5000)
RIGHT90_MANEUVER = (40, 3832)

RIGHT_WALL = (452, 4000)
LEFT_WALL = (0, 4000)

######################################################################################
######################################################################################
######################################################################################

errold = 0

atexit.register(hardware.close_all)


def maneuver(angle, encoder_ticks):
    hardware.steer(angle)
    start_tick = hardware.read_encoder()

    while True:
        hardware.forward()
        time.sleep(0.07)
        current_tick = hardware.read_encoder()
        if abs(current_tick - start_tick) > encoder_ticks:
            break
    hardware.stop_center()


def binarize(img, bin_min, bin_max):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bin_image = cv2.inRange(hsv, bin_min, bin_max)
    bin_image = cv2.erode(bin_image, None, iterations=4)
    bin_image = cv2.dilate(bin_image, None, iterations=4)

    return bin_image


def get_contour_params(cnt):
    M = cv2.moments(cnt)
    area = M['m00']
    cx = int(M['m10'] / area)
    cy = int(M['m01'] / area)

    return area, cx, cy


def detect_object(name, img, bin_min, bin_max, area_min, show=True):
    contour = None
    area, cx, cy = (None, None, None)

    binarized = binarize(img, bin_min, bin_max)
    debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)

    contours = cv2.findContours(binarized, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_NONE)[0]

    if len(contours) > 0:
        cv2.drawContours(debug, contours, -1, (0, 255, 0), 1)
        contours = list(
            filter(lambda c: cv2.contourArea(c) > area_min, contours))

        if len(contours) > 0:
            cv2.drawContours(debug, contours, -1, (0, 255, 0), 3)

            contour = max(contours, key=cv2.contourArea)
            area, cx, cy = get_contour_params(contour)

            cv2.drawContours(debug, [contour], -1, (0, 0, 255), 3)
            cv2.circle(debug, (cx, cy), 5, (0, 0, 255), -1)
    if show:
        cv2.imshow(name, debug)
    return contour, (area, cx, cy)


def wall():
    global errold
    l,r = hardware.read_sensors()


    r = round(r / ROUNDER) * ROUNDER

    err = (r - DISTANCE) 
    print("A:", l, r, err)
    # if math.fabs(err) < 2000:
    #     err = 0

    u = KP * err + KD * (err - errold)
    errold = err

    hardware.steer(u)


has_rotated = False

while True:
    start_time = time.time()
    # flag, img = hardware.get_frame()
    # if not flag: break

    # blue_line = detect_object(name="blue_line",
    #                           img=img[242:348, 74:285],
    #                           bin_min=(98, 66, 67),
    #                           bin_max=(149, 177, 166),
    #                           area_min=300)

    # orange_line = detect_object(name="orange_line",
    #                             img=img[300:384, 0:512],
    #                             bin_min=(90, 0, 0),
    #                             bin_max=(255, 255, 255),
    #                             area_min=300)

    # green = detect_object(name="green",
    #                       img=img[14:102, 321:396],
    #                       bin_min=(64, 227, 13),
    #                       bin_max=(90, 255, 39),
    #                       area_min=300)

    # if green[0] is not None:
    #     print(green[1])

    # blue_line_stop = blue_line[0] is not None
    # print(wall_forward)
    if not False:
        if 0 == 0:
            wall()
            hardware.forward()
            print("STATUS: RIDING_WALL")
        else:
            hardware.stop()

            print("Starting maneuver")
            time.sleep(5)
            print('Wowo!')
            maneuver(*LEFT90_MANEUVER)
            hardware.stop_center()
            has_rotated = True
        # time.sleep(600)

    ch = cv2.waitKey(5)
    if ch == 27:
        break

    print("Frame took:", time.time() - start_time)
