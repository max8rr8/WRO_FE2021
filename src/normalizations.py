import cv2
import numpy as np
from detection import crop

def normaliza_all(img, zone):
    img = img.copy()
    img = img.astype(np.float32)

    cropped = crop(img, zone)
    img -= np.min(cropped)

    cropped = crop(img, zone)
    img /= np.max(cropped)

    img[img < 0] = 0
    img[img > 1] = 1

    return (img * 255).astype(np.uint8)


def normaliza_channel(img, zone):
    img = img.copy()
    img = img.astype(np.float32)

    cropped = crop(img, zone)
    for c in [0, 1, 2]:
        img[:, :, c] -= np.min(cropped)

    cropped = crop(img, zone)
    for c in [0, 1, 2]:
        img[:, :, c] /= np.max(cropped)

    img[img < 0] = 0
    img[img > 1] = 1

    return (img * 255).astype(np.uint8)


def normaliza_half(img, zone):
    img = img.copy()
    img = img.astype(np.float32)

    cropped = crop(img, zone)
    img -= np.min(cropped)

    cropped = crop(img, zone)
    for c in [0, 1, 2]:
        img[:, :, c] /= np.max(cropped)

    img[img < 0] = 0
    img[img > 1] = 1

    return (img * 255).astype(np.uint8)
