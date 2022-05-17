from typing import List, Tuple
from pathlib import Path

import cv2

from .const import OUT_FPS as FPS
from .image_formatting import format_img


def stream_frames(path: Path):
    v = cv2.VideoCapture(str(path))
    while v.isOpened():
        r, frm = v.read()
        if not r:
            break
        yield frm
    v.release()


def save_frames(preview_zones: List[int], original_video: Path, frame_size: Tuple[int, int], fps: int) -> Path:
    preview_path = original_video.parent.joinpath(f"preview_{original_video.stem}.mp4")

    codec = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(preview_path), codec, FPS, frame_size)
    for idx, frame in enumerate(stream_frames(original_video)):
        if idx in preview_zones:
            formatted_frame = format_img(frame, idx, fps)
            out.write(formatted_frame)
    out.release()

    return preview_path


def get_fps(path: Path):
    video = cv2.VideoCapture(str(path))
    fps = int(video.get(cv2.CAP_PROP_FPS))
    video.release()
    return fps
