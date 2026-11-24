"""Print the pixel coordinates of every left mouse click on an image.

Useful for finding the corner points needed by warp_perspective.py.
"""

import cv2

from utils import resource_path


def mouse_points(event, x, y, flags, params):
    """Mouse callback: print the clicked (x, y) position on left click."""
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)


img = cv2.imread(resource_path("cards.png"))
cv2.imshow("Cards", img)

# Call mouse_points whenever a mouse event happens on the "Cards" window
cv2.setMouseCallback("Cards", mouse_points)

cv2.waitKey(0)
cv2.destroyAllWindows()
