import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
ap.add_argument(
    "-m", "--method",
    required=False,
    help="Method to blue image with (basic | gaussian | median | bilateral). Default is basic."
)
args = vars(ap.parse_args())

blurMethod = args["method"]
if blurMethod is None:
    blurMethod = "basic"
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

kernelSizes = [(3, 3), (9, 9), (15, 15)]

if blurMethod == "bilateral":
    params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

    for (diameter, sigmaColor, sigmaSpace) in params:
        blurred = cv2.bilateralFilter(image, diameter, sigmaColor, sigmaSpace)
        title = "Blurred d={}, sc={}, ss={}".format(diameter, sigmaColor, sigmaSpace)
        cv2.imshow(title, blurred)
        cv2.waitKey(0)
else:
    for (kX, kY) in kernelSizes:
        blurred = None
        if blurMethod == "basic":
            blurred = cv2.blur(image, (kX, kY))
        elif blurMethod == "gaussian":
            blurred = cv2.GaussianBlur(image, (kX, kY), 0)
        elif blurMethod == "median":
            blurred = cv2.medianBlur(image, kX)
        else:
            raise ValueError("Invalid blur method. Must one of (basic | gaussian | median | bilateral).")

        cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
        cv2.waitKey(0)
