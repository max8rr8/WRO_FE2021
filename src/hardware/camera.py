import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 384)


def set_resolution(fullhd):
    if fullhd:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    else:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 384)


def get_frame(show=True):
    # flag, img = (True, cv2.imread("./r0.png"))
    flag, img = cap.read()

    if not flag:
        return flag, None

    if img.shape[0] != 1080:
        img = img[:, :440]

    if show:
        cv2.imshow('img', img)

    return flag, img