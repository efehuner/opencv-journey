"""Interactive warp perspective: click 4 corners of the book to get a top-down view.

Click order: top-left, top-right, bottom-left, bottom-right.
Press 'r' to reset the points and 'q' to quit.
"""

import cv2
import numpy as np

from utils import resource_path

# Size of the output (bird's-eye view) image
WIDTH, HEIGHT = 250, 350

# Stores the 4 clicked corner points and how many have been clicked so far
points = np.zeros((4, 2), np.int32)
counter = 0


def mouse_points(event, x, y, flags, params):
    """Mouse callback: save the clicked position (up to 4 points)."""
    global counter
    if event == cv2.EVENT_LBUTTONDOWN and counter < 4:
        points[counter] = x, y
        counter += 1
        print(points)


img = cv2.imread(resource_path("book.png"))

cv2.namedWindow("Book")
cv2.setMouseCallback("Book", mouse_points)

while True:
    # Draw on a copy so the markers do not end up in the warped output
    img_display = img.copy()

    if counter == 4:
        src_points = np.float32(points)
        dst_points = np.float32([[0, 0], [WIDTH, 0], [0, HEIGHT], [WIDTH, HEIGHT]])

        matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        img_output = cv2.warpPerspective(img, matrix, (WIDTH, HEIGHT))
        cv2.imshow("Output", img_output)

    # Mark the points clicked so far
    for x, y in points[:counter]:
        cv2.circle(img_display, (int(x), int(y)), 15, (255, 0, 0), cv2.FILLED)

    cv2.imshow("Book", img_display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('r'):
        # Reset the selection and close the output window
        if counter == 4:
            cv2.destroyWindow("Output")
        counter = 0
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
