from skimage.metrics import structural_similarity as compare_ssim
import cv2
import numpy as np
import pyautogui
import time
from collections import deque


def capture_screen(region=None):
    """Capture a screenshot of the specified screen region."""
    screenshot = pyautogui.screenshot(region=region)
    # Consider resizing the screenshot to reduce processing time and memory usage
    screenshot = screenshot.resize((screenshot.width // 4, screenshot.height // 4))
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)


def compare_images(img1, img2):
    """Compare two images for similarity."""
    # Compute the Structural Similarity Index (SSI) between the two images
    ssi, _ = compare_ssim(img1, img2, full=True)
    return ssi


def main():
    print("Monitoring for repeated content on screen...")
    # Store screenshots for the last 60 seconds
    screenshots = deque(maxlen=30)  # Assuming a capture every second

    try:
        while True:
            current_img = capture_screen()
            # Compare current image with all images in the last minute
            repeat_detected = any(compare_images(current_img, past_img) > 0.96 for past_img in screenshots)

            if repeat_detected:
                print("Repeat detected. Pressing the right arrow key.")
                pyautogui.press('right')

            screenshots.append(current_img)
            time.sleep(0.5)  # Wait for 1 second before capturing again
    except KeyboardInterrupt:
        print("Program terminated.")

if __name__ == "__main__":
    main()
