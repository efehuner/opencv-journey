"""Shared helper functions for the OpenCV practice scripts."""

from pathlib import Path

import cv2
import numpy as np

# Absolute path to the "resources" folder, so scripts work from any working directory
RESOURCES_DIR = Path(__file__).resolve().parent.parent / "resources"


def resource_path(filename):
    """Return the absolute path (as a string) of a file inside the resources folder."""
    return str(RESOURCES_DIR / filename)


def stack_images(scale, img_array):
    """Stack multiple images into a single image grid.

    Args:
        scale: Scale factor applied to every image (e.g. 0.5 halves the size).
        img_array: Either a flat list of images (one row) or a list of lists
            (multiple rows). Grayscale images are converted to BGR automatically.

    Returns:
        A single numpy image containing all input images arranged in a grid.
    """
    rows = len(img_array)
    cols = len(img_array[0]) if isinstance(img_array[0], list) else 1
    rows_available = isinstance(img_array[0], list)

    # If a flat list was given, wrap it so it is treated as a single row
    if not rows_available:
        img_array = [img_array]
        rows = 1
        cols = len(img_array[0])

    # The first image defines the reference size for all others
    base_h, base_w = img_array[0][0].shape[:2]

    for x in range(rows):
        for y in range(cols):
            img = img_array[x][y]
            if img.shape[:2] == (base_h, base_w):
                img = cv2.resize(img, (0, 0), None, scale, scale)
            else:
                # Match the reference size first, then apply the scale
                img = cv2.resize(img, (base_w, base_h))
                img = cv2.resize(img, (0, 0), None, scale, scale)

            # hstack/vstack need the same number of channels, so convert grayscale to BGR
            if len(img.shape) == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

            img_array[x][y] = img

    if rows_available:
        # Stack each row horizontally, then stack the rows vertically
        horizontal_rows = [np.hstack(img_array[x]) for x in range(rows)]
        stacked = np.vstack(horizontal_rows)
    else:
        stacked = np.hstack(img_array[0])

    return stacked
