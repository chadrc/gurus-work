import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype="uint8")

red = (0, 0, 200)
green = (0, 200, 0)
blue = (200, 0, 0)
white = (255, 255, 255)


def show():
    cv2.imshow("Canvas", canvas)
    cv2.waitKey(0)


# Line
cv2.line(canvas, (0, 0), (300, 300), green)
show()

# With thickness
cv2.line(canvas, (300, 0), (0, 300), red, 3)
show()

# Rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
show()

# With thickness
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
show()

# Filled
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
show()

# Reset
canvas = np.zeros((300, 300, 3), dtype="uint8")

(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)

# Circle
for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white)

show()

canvas = np.zeros((300, 300, 3), dtype="uint8")

for i in range(0, 25):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 256, 3).tolist()
    pt = np.random.randint(0, 300, 2)

    cv2.circle(canvas, tuple(pt), radius, color, -1)

show()
