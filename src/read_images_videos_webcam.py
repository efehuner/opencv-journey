"""Read and display a video file frame by frame (use 0 instead of a path for the webcam)."""

import cv2

from utils import resource_path

FRAME_WIDTH = 640
FRAME_HEIGHT = 360

cap = cv2.VideoCapture(resource_path("Example-Video.mp4"))
# For a webcam, these set the capture size (3 = width, 4 = height)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

while True:
    success, img = cap.read()
    # Stop when the video ends or a frame cannot be read
    if not success:
        break

    img = cv2.resize(img, (FRAME_WIDTH, FRAME_HEIGHT))
    cv2.imshow("Video", img)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
