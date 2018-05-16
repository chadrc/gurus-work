import numpy as np
import argparse
import cv2

operation_set = "(erode | dilate | open | close | gradient | whitehat | blackhat)"
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
ap.add_argument("-o", "--operation", required=True, help="Morphological operation to perform {}.".format(operation_set))
ap.add_argument(
    "-s",
    "--shape",
    required=False,
    help="Kernel shape for the morphological operation (rect, cross, ellipse). Default is rect."
)
args = vars(ap.parse_args())

operation = args["operation"]
morph_option = args["shape"]

morph_shape = cv2.MORPH_RECT
if morph_option == "cross":
    morph_shape = cv2.MORPH_CROSS
elif morph_option == "ellipse":
    morph_shape = cv2.MORPH_ELLIPSE

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

for i in range(0, 3):
    modified = None
    iteration_count = i + 1
    copy = gray.copy()
    size = i * 2 + 3
    kernel_size = (size, size)

    kernel = cv2.getStructuringElement(morph_shape, kernel_size)

    if operation == "erode":
        modified = cv2.erode(copy, None, iterations=iteration_count)
    elif operation == "dilate":
        modified = cv2.dilate(copy, None, iterations=iteration_count)
    elif operation == "open":
        modified = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    elif operation == "close":
        modified = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    elif operation == "gradient":
        modified = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    elif operation == "whitehat":
        modified = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
    elif operation == "blackhat":
        modified = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, kernel)
    else:
        raise ValueError("Invalid operation. Must be one of {}.".format(operation_set))

    cv2.imshow("{} operation performed {} times".format(operation, i + 1), modified)
    cv2.waitKey(0)
