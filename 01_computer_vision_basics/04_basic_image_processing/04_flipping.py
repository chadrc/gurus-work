import numpy as np
import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# Resize so fits on screen
image = utils.resize(image, height=200)

(h, w) = image.shape[:2]

# Make canvas large enough for 2x2 of image
(canvasH, canvasW) = (h * 2, w * 2)
canvas = np.zeros((canvasH, canvasW, 3), dtype="uint8")

# Put original image in top left
canvas[0:h, 0:w] = image
# Flip vertically and put in top right
canvas[0:h, w:canvasW] = utils.flip_v(image)
# Flip horizontally and put in bottom left
canvas[h:canvasH, 0:w] = utils.flip_h(image)
# Flip horizontally and vertically and put in bottom right
canvas[h:canvasH, w:canvasW] = utils.flip_hv(image)

cv2.imshow("Flipping", canvas)
cv2.waitKey(0)
