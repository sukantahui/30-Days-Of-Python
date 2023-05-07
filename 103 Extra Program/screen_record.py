# Import necessary libraries:
import cv2
import numpy as np
import pyautogui
from win32api import GetSystemMetrics
import time

# Access screen width:
w = GetSystemMetrics(0)
# Access screen height:
h = GetSystemMetrics(1)
# Store screen dimensions within a tuple:
dimension = (w, h)
# Define codec -> FourCC is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# VideoWriter -> This class provides C++ API for writing video files or image sequences
# Constructor parameters-> video filename, video codec, video frame-rate(fps), screen dimensions
output = cv2.VideoWriter("recording.mp4", fourcc, 20.0, dimension)

# Access current system time:
now = time.time()
# Read screen recording duration via user input:
# time() -> Returns the time as a floating point number expressed in seconds
duration = int(input('Specify recording duration in seconds: '))
# Buffer time to ensure that the recorded video duration is as specified by user:
# This is done because, code must be executed up till line #33, prior to recording initiation.
duration += duration
# Identify the time at which recording must stop:
end_time = now + duration

while True:
    # Take a screenshot:
    # screenshot() -> Returns an Image object
    img = pyautogui.screenshot()
    # Import image data into NumPy array:
    frame = np.array(img)
    # Use cvtColor() method to convert image from BGR to RGB color format:
    # This conversion ensures that the recording exactly resembles the content that had been recorded
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Write the frame into the file 'recording.mp4':
    output.write(frame)
    # Access current system time:
    current_time = time.time()
    # Check if it is time to stop recording. If so, break out of while loop.
    if current_time>end_time:
        break

# Release the capture
output.release()