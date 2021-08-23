import cv2


import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*8, 3 ), np.float32)
objp[:,:2] = np.mgrid[0:8,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
cap = cv2.VideoCapture(0)
while True:
    flag, img = cap.read()
    print(img.shape)
    # print(icmg)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (8,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        print("DETECTED")
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (8,6), corners2, ret)


    cv.imshow('img', img)
    k = cv.waitKey(5000)
    if k == ord('w') and ret:
        print("WRITEN")
        objpoints.append(objp)
        imgpoints.append(corners)

    if k == ord('q'):
        break

# newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))
print(cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None))
cv.destroyAllWindows()