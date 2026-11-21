"""Create a blank image and draw shapes and text on it."""

import cv2
import numpy as np

# Black 512x512 image with 3 color channels (BGR)
img = np.zeros((512, 512, 3), dtype=np.uint8)

print(img.shape)

# Uncomment to fill the whole image with a single BGR color
# img[:] = 255, 149, 215

# Diagonal line from the top-left corner to the bottom-right corner
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (255, 149, 216), thickness=3)

# Filled blue rectangle (top-left point, bottom-right point)
cv2.rectangle(img, (350, 200), (450, 325), (255, 0, 0), thickness=cv2.FILLED)

# Filled green circle (center, radius)
cv2.circle(img, (100, 350), 50, (0, 255, 0), thickness=cv2.FILLED)

# Red text (bottom-left starting point, font, scale)
cv2.putText(img, "Hello World!", (250, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), thickness=3)

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
