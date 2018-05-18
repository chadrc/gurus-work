from skimage.filters import threshold_local
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to image file")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Image", image)

(T, threshInv) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary Inverse", threshInv)

(T, thresh) = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Binary", thresh)

cv2.imshow("Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Original", image)

(T, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold with Ostu value {}".format(T), threshInv)

cv2.imshow("Otsu Output", cv2.bitwise_and(image, image, mask=threshInv))
cv2.waitKey(0)
cv2.destroyAllWindows()

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 25)
cv2.imshow("OpenCV Mean Thresh", thresh)

T = threshold_local(blurred, 29, offset=5, method="gaussian")
thresh = (blurred < T).astype("uint8") * 255
cv2.imshow("scikit-image Mean Thresh", thresh)
cv2.waitKey(0)
