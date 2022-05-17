from itertools import chain

from scipy.signal import savgol_filter, find_peaks
import numpy as np
import pandas as pd


def get_frame_diff(frame: np.array, previous_frame: np.array):
    return (previous_frame - frame).mean()


def get_duration(frame_len: int, fps: int):
    return frame_len / (fps * 60)


def prepare_preview_zones(peaks, zone = 15, step = 3):
    peaks = pd.DataFrame({"middle": peaks})
    peaks.loc[:, "start_idx"] = (peaks.middle - zone).map(lambda x: max(x, 0))
    peaks.loc[:, "stop_idx"] = peaks.middle + zone
    return list(chain(*peaks.apply(lambda x: range(x.start_idx, x.stop_idx, step), axis = 1).values))


def get_preview_zones(diff: pd.Series, fps: int):
    
    filtered_diff = pd.Series(savgol_filter(diff, window_length=fps * 2, polyorder=2), index=diff.index)
    peaks, _ = find_peaks(filtered_diff, width = 20, height = 60)

    if peaks.size:
        return prepare_preview_zones(peaks)
    
    window = round(get_duration(diff.size, fps)) * fps
    rolling_mean = filtered_diff.rolling(window).mean().fillna(method="bfill")
    peaks = np.hstack([
        find_peaks(rolling_mean, width = window)[0], 
        find_peaks(-rolling_mean, width = window)[0]
    ])
    if peaks.size:
        return prepare_preview_zones(peaks)
    return []
