"""Resize and crop an image."""

import cv2

from utils import resource_path

img = cv2.imread(resource_path("Road.jpg"))

# shape = (height, width, channels)
print(img.shape)

# Note: cv2.resize expects (width, height)
width, height = 1000, 1000
img_resized = cv2.resize(img, (width, height))
print(img_resized.shape)

# Cropping is plain numpy slicing: img[y_start:y_end, x_start:x_end]
img_cropped = img[250:1280, 400:800]

# Scale the cropped part back up to the original image size
img_cropped_resized = cv2.resize(img_cropped, (img.shape[1], img.shape[0]))

# cv2.imshow("Road", img)
# cv2.imshow("Road Resized", img_resized)
cv2.imshow("Cropped Road", img_cropped)
cv2.imshow("Cropped and Resized Road", img_cropped_resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
