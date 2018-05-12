import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file.")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

(h, w) = image.shape[:2]
cv2.imshow("Original", image)

(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Read {r}, Green - {g}, Blue - {b}".format(r=r, g=g, b=b))

image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Read {r}, Green - {g}, Blue - {b}".format(r=r, g=g, b=b))

# Get center
(cX, cY) = (w // 2, h // 2)

tl = image[0:cY, 0:cX]
cv2.imshow("Top Left", tl)

tr = image[0:cY, cX:w]
cv2.imshow("Top Right", tr)

bl = image[cY:h, 0:cX]
cv2.imshow("Bottom Left", bl)

br = image[cY:h, cX:w]
cv2.imshow("Bottom Right", br)

# Change top left section to be green
image[0:cY, 0:cX] = (0, 255, 0)
cv2.imshow("Updated", image)

cv2.waitKey(0)
