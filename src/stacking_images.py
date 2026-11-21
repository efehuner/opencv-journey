"""Apply several filters to the webcam feed and show all results stacked in one window."""

import cv2
import numpy as np

from utils import stack_images

# --- Manual stacking example with numpy (kept for reference) ---
# img1 = cv2.imread(resource_path("lena.jpg"), 0)
# img2 = cv2.imread(resource_path("land.jpg"))
# img1 = cv2.resize(img1, (300, 300))
# img2 = cv2.resize(img2, (300, 300))
# img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)  # Channels must match before stacking
# hor = np.hstack((img1, img2))
# ver = np.vstack((img1, img2))
# cv2.imshow("Horizontal", hor)
# cv2.imshow("Vertical", ver)
# cv2.waitKey(0)

FRAME_WIDTH = 640
FRAME_HEIGHT = 360

# Kernel for dilation/erosion (created once, outside the loop)
kernel = np.ones((5, 5), dtype=np.uint8)

cap = cv2.VideoCapture(0)  # 0 = default webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))

    # Same pipeline as basic_functions.py, applied to every frame
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (7, 7), 0)
    img_canny = cv2.Canny(img_blur, 100, 200)
    img_dilation = cv2.dilate(img_canny, kernel, iterations=1)
    img_eroded = cv2.erode(img_dilation, kernel, iterations=1)

    # 2 rows x 3 columns grid of all processing steps
    img_stack = stack_images(1, [[img, img_gray, img_blur],
                                 [img_canny, img_dilation, img_eroded]])
    cv2.imshow("2x3 Stack", img_stack)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
