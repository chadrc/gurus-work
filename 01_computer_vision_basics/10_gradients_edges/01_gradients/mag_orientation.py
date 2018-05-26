import argparse
import numpy as np
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image.")
ap.add_argument("-l", "--lower-angle", type=float, default=175.0)
ap.add_argument("-u", "--upper-angle", type=float, default=180.0)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

gX = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
gY = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

mag = np.sqrt((gX ** 2) + (gY ** 2))
orientation = np.arctan2(gY, gX) * (180 / np.pi) % 180

idxs = np.where(orientation >= args["lower_angle"], orientation, -1)
idxs = np.where(orientation <= args["upper_angle"], idxs, -1)
mask = np.zeros(gray.shape, dtype="uint8")
mask[idxs > -1] = 255

cv2.imshow("Mask", mask)
cv2.waitKey(0)
