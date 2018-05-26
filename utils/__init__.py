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


def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    aspect = w / h

    if width is None and height is None:
        return image

    if width is not None:
        w = width
        h = width / aspect
    elif height is not None:
        w = height * aspect
        h = height

    resized = cv2.resize(image, (int(w), int(h)), interpolation=inter)

    return resized


def flip_h(image):
    return cv2.flip(image, 0)


def flip_v(image):
    return cv2.flip(image, 1)


def flip_hv(image):
    return cv2.flip(image, -1)


def auto_canny(image, sigma=0.3):
    v = np.median(image)

    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    return edged


def is_cv2():
    # if we are using OpenCV 2, then our cv2.__version__ will start
    # with '2.'
    return check_opencv_version("2.")


def is_cv3():
    # if we are using OpenCV 3.X, then our cv2.__version__ will start
    # with '3.'
    return check_opencv_version("3.")


def check_opencv_version(major, lib=None):
    # if the supplied library is None, import OpenCV
    if lib is None:
        import cv2 as lib

    # return whether or not the current OpenCV version matches the
    # major version number
    return lib.__version__.startswith(major)
