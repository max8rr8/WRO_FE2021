import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

import cv2
import numpy as np

cv2.startWindowThread()
iimg = 0
while iimg <= 13:
    img = cap.read()[1]
    img = img[0:400]
    cv2.imshow("img", img)
    # img = apply_brightness_contrast(img, 16, 16)
    # hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mi = np.min(img, axis=2)
    ma = np.max(img, axis=2)

    w = (ma - mi) < 20
    e = ma < 100

    wall = ((w * e) * 255).astype(np.uint8)

    wall = cv2.erode(wall, (8, 8), iterations=12)
    wall = cv2.dilate(wall, (8, 8), iterations=20)

    debug = np.zeros_like(img)

    debug[:, :, 2] = wall

    cv2.line(debug, (20, 1080), (20, 0), (0, 0, 255), 5)
    cv2.line(debug, (1900, 1080), (1900, 0), (0, 0, 255), 5)
    cv2.line(debug, (960, 1080), (960, 0), (0, 0, 255))

    mask = 255 - wall
    h, w, c = debug.shape
    cv2.floodFill(debug, np.zeros((h+2, w+2), dtype=np.uint8), (940, 199), (0, 255, 0))
    cv2.floodFill(debug, np.zeros((h+2, w+2), dtype=np.uint8), (980, 199), (0, 255, 0))




    prev_l = -1
    prev_r = -1 

    cnt_l = 0
    cnt_r = 0


    for i in reversed(range(400)):
        l = np.count_nonzero(debug[i, :960, 1])
        r = np.count_nonzero(debug[i, 960:, 1])

        if prev_l == -1:
            prev_l = l
        if prev_r == -1:
            prev_r = r

        if True:
            if l >= prev_l:
                cnt_l += abs(l - prev_l) + 0.2
            else:
                prev_l = l

            if r >= prev_r:
                cnt_r += abs(r - prev_r) + 0.2
            else:
                prev_r = r

    print(i, cnt_l, cnt_r)

    # cv2.imshow("img", img)
    # cv2.imshow("hsv", hsv)
    cv2.imshow("min", debug)

    if cv2.waitKey(1) == ord('n'):

        iimg += 1
