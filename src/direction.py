import cv2
import numpy as np
import hardware
from consts import *

def find_field(img):
    mi = np.min(img, axis=2)
    ma = np.max(img, axis=2)

    w = (ma - mi) < 20
    e = ma < 100

    wall1 = ((w * e) * 255).astype(np.uint8)

    wall1 = cv2.erode(wall1, (8, 8), iterations=12)
    wall1 = cv2.dilate(wall1, (8, 8), iterations=20)

    debug = np.zeros_like(img)

    debug[:, :, 2] = wall1

    cv2.line(debug, (20, 1080), (20, 0), (0, 0, 255), 5)
    cv2.line(debug, (1900, 1080), (1900, 0), (0, 0, 255), 5)
    cv2.line(debug, (960, 1080), (960, 0), (0, 0, 255))

    h, w, c = debug.shape
    cv2.floodFill(debug, np.zeros((h + 2, w + 2), dtype=np.uint8), (940, 199),
                  (0, 255, 0))
    cv2.floodFill(debug, np.zeros((h + 2, w + 2), dtype=np.uint8), (980, 199),
                  (0, 255, 0))

    cv2.imshow("Field", debug)

    return debug[:, :, 1]

def count(debug):
    cnt_l = 1
    cnt_r = 0
    
    prev_l = -1
    prev_r = -1


    for i in reversed(range(400)):
        l = np.count_nonzero(debug[i, :960])
        r = np.count_nonzero(debug[i, 960:])

        if prev_l == -1:
            prev_l = l
        if prev_r == -1:
            prev_r = r

        if l >= prev_l:
            cnt_l += abs(l - prev_l) + 0.2
        else:
            prev_l = l

        if r >= prev_r:
            cnt_r += abs(r - prev_r) + 0.2
        else:
            prev_r = r

    return cnt_l, cnt_r

def find_direction():
    cnt = []
    direction = None

    # while hardware.wait_button(ord(" ")):
    for i in range(10):
        flag, img = hardware.get_frame()
        field = find_field(img[:400])
        delta_cnt = count(field)
        
        cnt.append(delta_cnt)
        if len(cnt) >= 5:
            cnt = cnt[-5:]
        
        cnt_l = sum([c[0] for c in cnt])
        cnt_r = sum([c[1] for c in cnt])

        direction = cnt_r> cnt_l
        if direction == DIRECTION_CW:
            hardware.led(1,0, 0)
        else:
            hardware.led(0, 1,0)
    hardware.led(1,1,0)


    return direction
