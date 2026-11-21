"""Warp perspective: extract a single card from a photo and get a flat, top-down view of it."""

import cv2
import numpy as np

from utils import resource_path

img = cv2.imread(resource_path("cards.png"))

# Size of the output (bird's-eye view) image
WIDTH, HEIGHT = 250, 350

# Corner points of the card in the source image (top-left, top-right, bottom-left, bottom-right)
src_points = np.float32([[119, 232], [305, 196], [165, 511], [373, 466]])

# Where those corners should end up in the output image (same order)
dst_points = np.float32([[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]])

# Compute the 3x3 transformation matrix and apply it
matrix = cv2.getPerspectiveTransform(src_points, dst_points)
img_output = cv2.warpPerspective(img, matrix, (WIDTH, HEIGHT))

print(src_points)

# Mark the selected corner points on the original image with red dots
for x, y in src_points:
    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Cards", img)
cv2.imshow("Output", img_output)

cv2.waitKey(0)
cv2.destroyAllWindows()
