# Background Subtraction using OpenCV <img alt="GitHub" src="https://img.shields.io/github/license/nickPaterakis/background-subtraction">

This project demonstrates the use of OpenCV for background subtraction in video processing. The implemented algorithm can accurately detect moving objects in a video stream and draw bounding boxes around them.

## Usage

To use this project, you will need to have OpenCV installed in your system. You can then run the background_subtraction.py script by passing the path to your input video file as an argument. For example:

```
python background_subtraction.py --video_path ../your-video
```

The script will apply background subtraction to the video stream and display two windows: one showing the foreground and background masks and another showing the original RGB frame with bounding boxes around detected objects.

## Results
I have included a video in this repository that shows the results of applying the background subtraction algorithm to an input video. The algorithm is able to accurately track moving objects and create a clean foreground mask.
<div align="center">
  <img src="https://user-images.githubusercontent.com/36018286/129377035-c547d9ba-4a8d-44ff-ae12-5e0b42c25879.gif" width="500" />
</div>





