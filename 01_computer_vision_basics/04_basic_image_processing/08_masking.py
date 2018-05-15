import numpy as np
import argparse
import cv2

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


start = parse_coordinates(args["start"], (0, 0))
end = parse_coordinates(args["end"], (w, h))

mask = np.zeros((h, w), dtype="uint8")
cv2.rectangle(mask, start, end, 255, -1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Image", masked)

mask = np.zeros((h, w), dtype="uint8")
smallest_dim = w // 2 if w < h else h // 2
cv2.circle(mask, (w // 2, h // 2), smallest_dim, 255, -1)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Masked Circle", masked)

cv2.waitKey(0)
