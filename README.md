# OpenCV Journey 👁️

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5.x-green?logo=opencv&logoColor=white)
![Status](https://img.shields.io/badge/status-in%20progress-orange)

My step-by-step journey of learning computer vision with [OpenCV](https://opencv.org/) and Python.
Each script focuses on a single concept, and new topics are added as I progress.

## Project Structure

```
OpenCV/
├── resources/                        # Sample images and video used by the scripts
├── src/
│   ├── utils.py                      # Shared helpers (resource paths, image stacking)
│   ├── read_images_videos_webcam.py  # Read and play a video file / webcam
│   ├── basic_functions.py            # Grayscale, blur, Canny edges, dilation, erosion
│   ├── resize_cropping.py            # Resizing and cropping images
│   ├── blank_image_shapes_text.py    # Draw lines, rectangles, circles and text
│   ├── warp_perspective.py           # Bird's-eye view of a card with perspective transform
│   ├── stacking_images.py            # Live webcam filters shown in a single stacked window
│   ├── color_detection.py            # HSV color detection tuned with trackbars
│   ├── mouse_points.py               # Print pixel coordinates of mouse clicks
│   ├── mouse_points_implementation.py # Click 4 corners to warp a book interactively
│   └── contours_detection.py         # Live contour detection with points and area
├── requirements.txt
└── README.md
```

## Getting Started

### Requirements

- Python 3.10+
- A webcam (only for `stacking_images.py`, `color_detection.py` and `contours_detection.py`)

### Installation

```bash
git clone https://github.com/efehuner/opencv-journey.git
cd opencv-journey

python -m venv venv

# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install -r requirements.txt
```

### Running a Script

```bash
python src/basic_functions.py
```

Scripts locate the `resources` folder automatically, so they can be run from any directory.
Close image windows with any key; for video/webcam scripts press **`q`** to quit.
In `mouse_points_implementation.py` click the corners in order (top-left, top-right, bottom-left, bottom-right), press **`r`** to reset.

## Topics Covered

| Script                         | Topic                                                  |
| ------------------------------ | ------------------------------------------------------ |
| `read_images_videos_webcam.py` | `VideoCapture`, reading frames, keyboard exit          |
| `basic_functions.py`           | `cvtColor`, `GaussianBlur`, `Canny`, `dilate`, `erode` |
| `resize_cropping.py`           | `resize`, numpy slicing for cropping                   |
| `blank_image_shapes_text.py`   | `line`, `rectangle`, `circle`, `putText`               |
| `warp_perspective.py`          | `getPerspectiveTransform`, `warpPerspective`           |
| `stacking_images.py`           | Combining multiple images with `hstack` / `vstack`     |
| `color_detection.py`           | HSV color space, `createTrackbar`, `inRange`, `bitwise_and` |
| `mouse_points.py`              | `setMouseCallback`, mouse events                       |
| `mouse_points_implementation.py` | Interactive perspective warp with mouse clicks       |
| `contours_detection.py`        | `findContours`, `contourArea`, `approxPolyDP`, `boundingRect` |

## Roadmap

- [x] Reading images, videos and webcam
- [x] Basic image processing functions
- [x] Resizing and cropping
- [x] Drawing shapes and text
- [x] Warp perspective
- [x] Stacking images
- [x] Color detection
- [x] Mouse events
- [x] Contours and shape detection
- [ ] Face detection

## License

This project is intended for educational purposes.
