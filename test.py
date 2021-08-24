import hardware
import cv2

while True:
  _, f = hardware.get_frame(False)
  f = cv2.flip(f, 1)
  cv2.line(f, (f.shape[1] // 2, 0), (f.shape[1] // 2, 400), (0, 255,255), 2) 
  cv2.imshow("a", f)
  cv2.waitKey(5)