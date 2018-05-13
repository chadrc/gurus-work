import numpy as np
import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

resized = utils.resize(image, width=200)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

resized = utils.resize(image, height=300)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
