# Telegram Video Auto-Advancer

## Description
This Python script automatically moves to the next video in Telegram when the current video ends. It uses image processing to detect when the same frame appears repeatedly, indicating that a video has stopped playing. This removes the need to manually click the right arrow to proceed to the next video.

## Features
- **Automatic Video Advancement:** Moves to the next video without user interaction.
- **Screen Capture:** Captures screenshots to analyze the video content.
- **Image Comparison:** Uses Structural Similarity Index (SSI) to detect when the video content has not changed.

## Requirements
- Python 3.x
- Libraries: `skimage`, `cv2`, `numpy`, `pyautogui`, `time`, `collections`

## Installation
To set up this script, you need to install the required Python libraries. You can install these using pip:

```bash
pip install scikit-image opencv-python numpy pyautogui
```

Usage
Run the script from the command line by navigating to the directory containing the script and executing:

```bash
python telegram_auto_advance.py
```


Ensure that the Telegram video player is visible on your screen as the script monitors the screen area where the video is displayed.

## How It Works
The script captures a portion of the screen where the Telegram video is played.
It continuously compares the current screenshot with previous ones to detect if the same frame is showing for an extended period.
If a repeat frame is detected, indicating that the video has stopped, the script simulates a right arrow key press to move to the next video.

## Safety and Performance Notes
The script modifies screenshot resolution to improve performance and reduce memory usage.
Ensure that the screen area is correctly specified for the video player in your Telegram application.

## Limitations
The script needs to be manually terminated with a KeyboardInterrupt (Ctrl+C).
It is necessary to adjust the region of the screen capture depending on where the Telegram video is played on your screen.
