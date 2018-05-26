import numpy as np
import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", image)

contours = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if utils.is_cv2() else contours[1]
clone = image.copy()
cv2.drawContours(clone, contours, -1, (0, 255, 0), 2)
print("Found {} contours".format(len(contours)))

cv2.imshow("Contours", clone)
cv2.waitKey(0)
