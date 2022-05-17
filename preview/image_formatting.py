from datetime import timedelta

import cv2
import numpy as np

from .const import Colors


def id_to_timecode(id: int, fps: int):
    return str(timedelta(seconds=id / fps)).split(".")[0]


def format_img(img: np.array, idx: int, fps: int):
    h, w, _ = img.shape
    cv2.rectangle(
        img,
        (0, h),
        (w, h - 25),
        Colors.timecode_background.value,
        cv2.FILLED
    )
    cv2.putText(
        img,
        id_to_timecode(idx, fps),
        (0, h),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        Colors.timecode_font.value,
        2
    )
    return img
