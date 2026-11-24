"""Color detection in HSV space with live trackbars to tune the color range."""

import cv2
import numpy as np

FRAME_WIDTH = 640
FRAME_HEIGHT = 480


def empty(_):
    """Dummy callback required by cv2.createTrackbar."""
    pass


cap = cv2.VideoCapture(0)  # 0 = default webcam
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

# Window with trackbars for the lower/upper HSV limits
# Note: in OpenCV, Hue ranges from 0-179, Saturation and Value from 0-255
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue Min", "HSV", 0, 179, empty)
cv2.createTrackbar("Hue Max", "HSV", 179, 179, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("Value Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Value Max", "HSV", 255, 255, empty)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))

    # HSV makes it much easier to select a color than BGR
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Read the current trackbar positions
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Value Min", "HSV")
    v_max = cv2.getTrackbarPos("Value Max", "HSV")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Mask: white where the pixel is inside the range, black otherwise
    mask = cv2.inRange(img_hsv, lower, upper)

    # Keep only the pixels of the original image that are inside the mask
    result = cv2.bitwise_and(img, img, mask=mask)

    # Convert the mask to 3 channels so it can be stacked with the color images
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    img_stack = np.hstack([img, mask_bgr, result])

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV Color Space", img_hsv)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", result)
    cv2.imshow("Original | Mask | Result", img_stack)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
