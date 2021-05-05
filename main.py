import datetime

from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
# Formatting String
file_name = f'{time_stamp}.mp4'

# Encoding and decoding for video writing ability
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))

# Capturing video from the webcam
webcam = cv2.VideoCapture(0)

while True:
    # Capturing the image of the screen continuously
    # bbox is the boundary box (Eg. whole screen, part of the screen, etc.)
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    # Converting into numpy array
    img_np = np.array(img)
    # Converting to RGB Color
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # Reading the video from the webcam
    _, frame = webcam.read()
    # print("frame:", frame)
    # print("img_final:", img_final)
    frame_height, frame_width, _ = frame.shape
    # To fix the video from the webcam in the img_final. We can see the video from the webcam even
    # when we change the tab, which wasn't the case otherwise.
    img_final[0: frame_height, 0: frame_width, :] = frame[0: frame_height, 0: frame_width, :]
    # imshow(Name of the screen, the array you want to show)
    cv2.imshow('Secret Capture', img_final)
    # cv2.imshow('Webcam', frame)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break


