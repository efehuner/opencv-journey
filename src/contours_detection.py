"""Detect contours (shapes) in the webcam feed and show their corner points and area.

Trackbars:
    Threshold1 / Threshold2 - Canny edge detection thresholds
    Min Area                - contours smaller than this area are ignored
"""

import cv2
import numpy as np

from utils import stack_images

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Hard lower limit for the "Min Area" trackbar, so tiny noise contours are never shown
MIN_AREA_LIMIT = 500
MAX_AREA_LIMIT = 30000


def empty(_):
    """Dummy callback required by cv2.createTrackbar."""
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 150, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 255, 255, empty)
cv2.createTrackbar("Min Area", "Parameters", 5000, MAX_AREA_LIMIT, empty)
cv2.setTrackbarMin("Min Area", "Parameters", MIN_AREA_LIMIT)

cap = cv2.VideoCapture(0)  # 0 = default webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# Kernel for dilation (created once, outside the loop)
kernel = np.ones((5, 5), dtype=np.uint8)


def get_contours(img, img_contour, min_area):
    """Find external contours in a binary image and draw them on img_contour.

    For every contour larger than min_area, draws the contour, its bounding box,
    and writes the number of corner points and the area next to it.
    """
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        # Minimum area check: skip small contours (usually noise)
        if area < max(min_area, MIN_AREA_LIMIT):
            continue

        cv2.drawContours(img_contour, [cnt], -1, (255, 0, 255), 7)

        # Approximate the contour with a polygon; the number of vertices
        # tells us the shape (3 = triangle, 4 = rectangle, many = circle ...)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 5)

        # Show the number of points and the area to the right of the bounding box
        cv2.putText(img_contour, f"Points: {len(approx)}", (x + w + 20, y + 20),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(img_contour, f"Area: {int(area)}", (x + w + 20, y + 45),
                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
    img_contour = img.copy()  # Contours are drawn on a copy, the original stays clean

    img_blur = cv2.GaussianBlur(img, (7, 7), 1)
    img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    # Read the current trackbar values
    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    min_area = cv2.getTrackbarPos("Min Area", "Parameters")

    img_canny = cv2.Canny(img_gray, threshold1, threshold2)

    # Dilation closes small gaps in the edges so contours are detected as one piece
    img_dilation = cv2.dilate(img_canny, kernel, iterations=1)

    get_contours(img_dilation, img_contour, min_area)

    img_stack = stack_images(0.8, [[img, img_blur, img_gray],
                                   [img_canny, img_dilation, img_contour]])
    cv2.imshow("Result", img_stack)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
