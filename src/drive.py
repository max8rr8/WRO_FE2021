import cv2
import numpy as np
import hardware

AUTOHSV_MARGIN = 10

hardware.stop_center()
# hardware.set_custom_resolution((640,480))
cv2.namedWindow("Control")


def draw_text(img, text, x, y, color=(255, 255, 255)):
  textsize = cv2.getTextSize(text, cv2.FONT_HERSHEY_PLAIN, 2, 2)[0]
  textX = int(x - textsize[0] / 2)
  textY = int(y + textsize[1] / 2)

  cv2.putText(img, text, (textX, textY), cv2.FONT_HERSHEY_PLAIN, 2, color, 2)


steer_status = "STOP"


def draw_steer_control():
  img = np.zeros((100, 480, 3))

  p = 80

  c = (0, 0, 255)
  if steer_status == "Forward": c = (0, 255, 0)
  if steer_status == "Reverse": c = (255, 0, 0)

  for text in ["Reverse", "STOP", "Forward"]:
    text_collor = c if text == steer_status else (255, 255, 255)
    draw_text(img, text, p, 50, color=text_collor)

    p += 160

    if p < 480:
      cv2.line(img, (p - 80, 0), (p - 80, 100), c, 2)

  cv2.imshow("Control", img)


def set_steer_control(event, x, y, flags, param):
  global steer_status
  if event == cv2.EVENT_LBUTTONDOWN:
    if x < 160:
      steer_status = "Reverse"
    elif x < 320:
      steer_status = "STOP"
    else:
      steer_status = "Forward"


cv2.setMouseCallback("Control", set_steer_control)

cv2.createTrackbar("Angle", "Control", 0, 100, lambda x: x)
cv2.setTrackbarPos("Angle", "Control", 50)

while True:
  draw_steer_control()
  
  f, frame = hardware.get_frame()
#   cv2.imshow("Frame", frame)

  key = cv2.waitKey(1)

  if key == 27:
    break

  elif key == ord("w"):

    if steer_status == "STOP":
      steer_status = "Forward"
    elif steer_status == "Reverse":
      steer_status = "STOP"

  elif key == ord("s"):

    if steer_status == "STOP":
      steer_status = "Reverse"
    elif steer_status == "Forward":
      steer_status = "STOP"

  elif key == ord("a"):
    cv2.setTrackbarPos("Angle", "Control",
                       cv2.getTrackbarPos("Angle", "Control") - 25)

  elif key == ord("d"):
    cv2.setTrackbarPos("Angle", "Control",
                       cv2.getTrackbarPos("Angle", "Control") + 25)

  elif key == ord("e"):
    cv2.setTrackbarPos("Angle", "Control", 50)

  elif key == ord("q"):
    steer_status = "STOP"

  if steer_status == "STOP":
    hardware.set_direction(True)
    hardware.stop()
  elif steer_status == "Forward":
    hardware.set_direction(True)
    hardware.forward()
  elif steer_status == "Reverse":
    hardware.set_direction(False)
    hardware.stop()

  hardware.steer(cv2.getTrackbarPos("Angle", "Control") - 50)

  if key != -1:
    print(key, steer_status)

cv2.destroyAllWindows()