import numpy as np
import cv2


def translate(image, x, y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, mat, (image.shape[1], image.shape[0]))

    return shifted


def rotate(image, deg, center=None, scale=1.0):
    (h, w) = image.shape[:2]

    if center is None:
        center = (w / 2, h / 2)

    mat = cv2.getRotationMatrix2D(center, deg, scale)
    rotated = cv2.warpAffine(image, mat, (w, h))

    return rotated

