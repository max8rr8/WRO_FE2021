
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)


# def normalize(img):
#     img = img.copy()
#     for i in range(3):
#         normalization = img[:, :, i]
#         mi = np.min(normalization)
#         ma = np.max(normalization)

#         im = img[:, :, i].astype(np.float32) - mi
#         im /= ma - mi
#         im = np.clip(im, 0, 1)
#         img[:, :, i] = (im * 255).astype(np.uint8)
#     cv2.imshow("NORMALIZED", img)
#     return img

i = 0
while True:
  a, b = cap.read()
  # print(a, b)
  b= b[:, :, ::-1]
  cv2.imshow("b", b)
  # normalize(b)
  k = cv2.waitKey(5)
  if k == ord('s'):
    cv2.imwrite(f"image{i}.png", b)
    i += 1