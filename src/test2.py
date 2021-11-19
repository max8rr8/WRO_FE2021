import cv2
import numpy as np
import picamera
import time

from picamera.array import PiRGBArray
from picamera import PiCamera

def detect(img):
    hsv_min = np.array([20,100,80])
    hsv_max = np.array([27,255,255])
    masked = cv2.inRange(img, hsv_min, hsv_max)

    return masked


def main():
    #camera mode
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 20
    camera.awb_mode = 'fluorescent'
    camera.awb_gains = 4
    camera.exposure_mode = 'off'
    capture = PiRGBArray(camera, size=(640, 480))

    # allow the camera to warmup
    time.sleep(0.1)

    for frame in camera.capture_continuous(capture, format="bgr", use_video_port=True):
        image = frame.array
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        mask = detect(hsv)

        label = cv2.connectedComponentsWithStats(mask)

        cv2.imshow("Image", image)
        cv2.imshow("Mask", mask)

        key = cv2.waitKey(1) & 0xFF
        capture.truncate(0)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main() 