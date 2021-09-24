import cv2
import numpy as np
import hardware

AUTOHSV_MARGIN = 10

hardware.stop_center()

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

cv2.createTrackbar("Angle", "Control", 0, 50, lambda x: x)
cv2.setTrackbarMin("Angle", "Control", -50)
cv2.setTrackbarPos("Angle", "Control", 0)

#############
detection_params = {
    "x1": 0,
    "y1": 0,
    "x2": 512,
    "y2": 384,
    "h_min": 0,
    "s_min": 0,
    "v_min": 0,
    "h_max": 255,
    "s_max": 255,
    "v_max": 255,
    "area_min": 300
}

cv2.imshow("Detection", np.zeros((1, 640)))


def creat_trackbar(param, val):
  max_val = 255
  if param[0] == "x": max_val = 512
  if param[0] == "y": max_val = 384
  if param == "area_min": max_val = 10000

  def change(x):
    detection_params[param] = x

  cv2.createTrackbar(param, "Detection", 0, max_val, change)
  cv2.setTrackbarPos(param, "Detection", int(val))


def binarize(img, bin_min, bin_max):
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
  
  hsv[:, :, 0][hsv[:, :, 0] > 170] = 0
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


def detect_object(name, img, bin_min, bin_max, area_min):
  contour = None
  area, cx, cy = (None, None, None)

  binarized = binarize(img, bin_min, bin_max)
  debug = cv2.cvtColor(binarized, cv2.COLOR_GRAY2BGR)

  contours = cv2.findContours(binarized, cv2.RETR_TREE,
                              cv2.CHAIN_APPROX_NONE)[0]

  if len(contours) > 0:
    cv2.drawContours(debug, contours, -1, (0, 255, 0), 1)
    contours = list(filter(lambda c: cv2.contourArea(c) > area_min, contours))

    if len(contours) > 0:
      cv2.drawContours(debug, contours, -1, (0, 255, 0), 3)

      contour = max(contours, key=cv2.contourArea)
      area, cx, cy = get_contour_params(contour)

      cv2.drawContours(debug, [contour], -1, (0, 0, 255), 3)
      cv2.circle(debug, (cx, cy), 5, (0, 0, 255), -1)

  # cv2.imshow(name, debug)
  return contour, debug


cv2.namedWindow("Detection")

for param, val in detection_params.items():
  creat_trackbar(param, val)


def get_detection_params():
  return {
      "bin_min": (detection_params["h_min"], detection_params["s_min"],
                  detection_params["v_min"]),
      "bin_max": (detection_params["h_max"], detection_params["s_max"],
                  detection_params["v_max"]),
      "area_min":
      detection_params["area_min"]
  }


selecting_area = False
selecting_hsv = False

hsv_area = [(0, 0), (0, 0)]


def detection_buttons():
  img = np.zeros((80, 880, 3))

  p = 128

  c = (0, 255, 0)

  if selecting_area or selecting_hsv:
    draw_text(img, "Selectring AREA" if selecting_area else "Auto HSV", 512,
              40)
    img[78:80, :] = (0, 255, 0)
    return img.astype(np.uint8)

  for text in ["Select AREA", "Auto HSV", "Export", ""]:
    text_collor = (255, 255, 255)
    draw_text(img, text, p, 40, color=text_collor)

    p += 256

    if p < 880:
      cv2.line(img, (p - 128, 0), (p - 128, 128), c, 2)

  img[78:80, :] = (0, 255, 0)

  return img.astype(np.uint8)


def draw_detection_configuration():
  flag, img = hardware.get_frame(False)

  debug = np.zeros(img.shape, np.uint8)
  debug[:, :, 0] = 255

  try:
    cnt, det_debug = detect_object(
        "Detection", img[detection_params["y1"]:detection_params["y2"],
                         detection_params["x1"]:detection_params["x2"]],
        **get_detection_params())

    debug[detection_params["y1"]:detection_params["y2"],
          detection_params["x1"]:detection_params["x2"]] = det_debug

  except:
    print("Failed to detect object")

  cv2.rectangle(img, (detection_params["x1"], detection_params["y1"]),
                (detection_params["x2"], detection_params["y2"]), (0, 255, 0),
                2)

  if selecting_hsv:
    cv2.rectangle(img, hsv_area[0], hsv_area[1], (0, 0, 255), 2)

  img = cv2.hconcat([img, debug])
  buttons = detection_buttons()
  # print(img.shape, detection_buttons().shape)
  img = cv2.vconcat([buttons, img])

  cv2.imshow("Detection2", img)
  # cv2.imshow("Debug", debug)

cv2.namedWindow("Detection2")
selector_first_pressed = False


def autohsv(img):
  hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  h_min = max(np.min(hsv[:, :, 0]) - AUTOHSV_MARGIN, 0)
  s_min = max(np.min(hsv[:, :, 1]) - AUTOHSV_MARGIN, 0)
  v_min = max(np.min(hsv[:, :, 2]) - AUTOHSV_MARGIN, 0)

  h_max = min(np.max(hsv[:, :, 0]) + AUTOHSV_MARGIN, 255)
  s_max = min(np.max(hsv[:, :, 1]) + AUTOHSV_MARGIN, 255)
  v_max = min(np.max(hsv[:, :, 2]) + AUTOHSV_MARGIN, 255)

  cv2.setTrackbarPos("h_min", "Detection", h_min)
  cv2.setTrackbarPos("s_min", "Detection", s_min)
  cv2.setTrackbarPos("v_min", "Detection", v_min)
  cv2.setTrackbarPos("h_max", "Detection", h_max)
  cv2.setTrackbarPos("s_max", "Detection", s_max)
  cv2.setTrackbarPos("v_max", "Detection", v_max)


def export_detection():
  bin_min = (detection_params["h_min"], detection_params["s_min"],
             detection_params["v_min"])
  bin_max = (detection_params["h_max"], detection_params["s_max"],
             detection_params["v_max"])

  crop = f'(({detection_params["y1"]}, {detection_params["y2"]}), ({detection_params["x1"]}, {detection_params["x2"]}))'

  print(f"    'zone': {crop},")
  print(f"    'bin_min': {bin_min},")
  print(f"    'bin_max': {bin_max},")
  print(f"    'area_min': {detection_params['area_min']}")


def detection_button(event, x, y, flags, param):
  global selector_first_pressed
  global selecting_area
  global selecting_hsv
  global hsv_area
  
  if event == cv2.EVENT_LBUTTONDOWN:
    if y < 80:
      flag, img = hardware.get_frame(show=False)

      selector_first_pressed = False
      if x < 256:
        selecting_area = True
      elif x < 512:
        hsv_area = [(0,0),(0,0)]
        selecting_hsv = True
      else:
        export_detection()

    else:
      y -= 80
      if x < 512 and y > 0:
        selector_first_pressed = True

        if selecting_area:
          cv2.setTrackbarPos("x1", "Detection", x)
          cv2.setTrackbarPos("y1", "Detection", y)
        if selecting_hsv:
          hsv_area[0] = (x, y)

  elif event == cv2.EVENT_MOUSEMOVE:
    if selector_first_pressed:
      y -= 80
      if x < 512 and y > 0:
        if selecting_hsv:
          hsv_area[1] = (x, y)

        if selecting_area and x > detection_params[
            "x1"] and y > detection_params["y1"]:
          cv2.setTrackbarPos("x2", "Detection", x)
          cv2.setTrackbarPos("y2", "Detection", y)

  elif event == cv2.EVENT_LBUTTONUP:
    if selector_first_pressed:
      selecting_area = False

      if selecting_hsv:
        flag, img = hardware.get_frame(show=False)
        print(hsv_area)
        x1, y1 = hsv_area[0]
        x2, y2 = hsv_area[1]
        try:
          autohsv(img[y1:y2, x1:x2])
        except:
          pass
        selecting_hsv = False


cv2.setMouseCallback("Detection2", detection_button)

# cv2.createTrackbar("Detection", "x1", 0, 512, lambda x: x1)

while True:
  draw_steer_control()
  draw_detection_configuration()

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
    cv2.setTrackbarPos("Angle", "Control", 0)

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

  hardware.steer(cv2.getTrackbarPos("Angle", "Control"))

  if key != -1:
    print(key, steer_status)

cv2.destroyAllWindows()