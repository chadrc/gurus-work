import numpy as np
import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)

rotated = utils.rotate(image, 45)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

rotated = utils.rotate(image, -90)
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)

rotated = utils.rotate(image, 45, (cX - 50, cY - 50))
cv2.imshow("Rotated", rotated)
cv2.waitKey(0)
