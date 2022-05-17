# Video preview generator

Generation of the video preview based on frame change. If there are significant changes, the moment is worth human attention.

Tested on `mp4` files only.

## Prerequisites

Python 3.8+

```
apt-get update
apt-get install ffmpeg libsm6 libxext6  -y
pip install opencv-python scipy pandas
```

## Run

```
python main.py /home/user/Downloads/video.mp4 /home/user/Downloads/video_2.mp4
```

Expected output:

```
[2022-05-17 22:11:16,176][INFO] File #1: /home/user/Downloads/video.mp4
[2022-05-17 22:11:16,177][INFO] Reading file /home/user/Downloads/video.mp4...
[2022-05-17 22:11:16,183][INFO] FPS: 30
[2022-05-17 22:11:17,512][INFO] Duration of video file /home/user/Downloads/video.mp4: ~0:00:10
[2022-05-17 22:11:17,512][INFO] Getting preview zones...
[2022-05-17 22:11:17,517][INFO] Duration of preview: ~0:00:03
[2022-05-17 22:11:18,076][INFO] Saving file /home/user/Downloads/preview_video.mp4...
[2022-05-17 22:11:18,076][INFO] File #2: /home/user/Downloads/video_2.mp4
[2022-05-17 22:11:18,076][INFO] Reading file /home/user/Downloads/video_2.mp4...
[2022-05-17 22:11:18,088][INFO] FPS: 30
[2022-05-17 22:11:19,750][INFO] Duration of video file /home/user/Downloads/video_2.mp4: ~0:10:38
[2022-05-17 22:11:19,750][INFO] Getting preview zones...
[2022-05-17 22:11:19,754][INFO] Duration of preview: ~0:00:12
[2022-05-17 22:11:20,731][INFO] Saving file /home/user/Downloads/preview_video_2.mp4...
```

If the preview generation went successfully, a new file with the prefix "preview_" should appear in the same folder.

## Help
```
python main.py --help
```