import numpy as np
import argparse
import cv2
import utils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
ap.add_argument("-s", "--start", required=False, help="Coordinates to start crop")
ap.add_argument("-e", "--end", required=False, help="Coordinates to end crop")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)
(h, w) = image.shape[:2]


def parse_coordinates(coordinate, default):
    if coordinate is None:
        return default

    try:
        (x, y) = tuple([int(part) for part in coordinate.split(",")])
        if x > w or x < 0 or y > h or y < 0:
            raise ValueError

        return x, y
    except ValueError:
        print("Invalid start coordinates")
        exit(1)


(sX, sY) = parse_coordinates(args["start"], (0, 0))
(eX, eY) = parse_coordinates(args["end"], (w, h))

cropped = image[sY:eY, sX:eX]
cv2.imshow("Cropped", cropped)
cv2.waitKey(0)
