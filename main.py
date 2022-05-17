import logging
from pathlib import Path
import logging

import pandas as pd

from preview import stream_frames, save_frames, get_frame_diff, get_preview_zones, id_to_timecode, get_fps
from preview.const import OUT_FPS

logging.basicConfig(level=logging.INFO, format='[%(asctime)s][%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)


def main(path: Path):

    if not path.exists():
        logger.error(f"{path} not found.")
        return None

    logger.info(f"Reading file {path}...")
    fps = get_fps(path)
    logger.info(f"FPS: {fps}")
    previous_frame = None
    diff = pd.Series(name="diff", dtype="float32")
    for idx, frame in enumerate(stream_frames(path)):
        if previous_frame is not None:
            diff.loc[idx] = get_frame_diff(frame, previous_frame)
        previous_frame = frame
    logger.info(f"Duration of video file {path}: ~{id_to_timecode(idx, fps)}")
    
    logger.info(f"Getting preview zones...")
    preview_zones = get_preview_zones(diff, fps)
    logger.info(f"Duration of preview: ~{id_to_timecode(len(preview_zones), OUT_FPS)}")
    
    if preview_zones:
        frame_size = frame.shape[:-1][::-1]
        preview_path = save_frames(
            preview_zones=preview_zones, 
            original_video=path, 
            frame_size=frame_size, 
            fps=fps
        )
        logger.info(f"Saving file {preview_path}...")
    else:
        logger.error(f"Preview not generated.")
        return None


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('fp', type=Path, nargs='+', help='path to video file(s)')
    
    args = parser.parse_args()
    
    for file_idx, fp in enumerate(args.fp, start=1):
        logger.info(f"File #{file_idx}: {fp}")
        main(fp)
