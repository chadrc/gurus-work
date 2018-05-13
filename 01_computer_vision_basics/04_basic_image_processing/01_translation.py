import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

shifted = utils.translate(image, 25, 50)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)

shifted = utils.translate(image, -50, -90)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)

shifted = utils.translate(image, 0, 100)
cv2.imshow("Shifted", shifted)
cv2.waitKey(0)
