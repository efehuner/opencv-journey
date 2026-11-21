"""Basic OpenCV functions: grayscale, blur, edge detection, dilation and erosion."""

import cv2
import numpy as np

from utils import resource_path

path = resource_path("lena.jpg")

# 5x5 kernel of ones used for the dilation and erosion operations
kernel = np.ones((5, 5), dtype=np.uint8)

img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                        # Convert to grayscale
img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)                        # Smooth the image
img_canny = cv2.Canny(img_blur, 100, 200)                               # Detect edges
img_dilation = cv2.dilate(img_canny, kernel, iterations=1)              # Thicken the edges
img_eroded = cv2.erode(img_dilation, kernel, iterations=1)              # Thin the edges back

cv2.imshow("Lena", img)
cv2.imshow("Grayscale", img_gray)
cv2.imshow("Blur", img_blur)
cv2.imshow("Canny", img_canny)
cv2.imshow("Dilation", img_dilation)
cv2.imshow("Eroded", img_eroded)

# Wait until any key is pressed, then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
