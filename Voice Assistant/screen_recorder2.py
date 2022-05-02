import numpy as np
import cv2
import datetime
from win32api import GetSystemMetrics
from PIL import ImageGrab


def screen_recorder2():
    width = GetSystemMetrics(0)  # screen's width
    height = GetSystemMetrics(1)  # screen's height

    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # creating dynamic file name using time
    file_name = f'{time_stamp}.mp4'  # creating dynamic file name using time

    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # encoding
    captured_video = cv2.VideoWriter(file_name, fourcc, 15.0, (width, height))

    while True:
        img = ImageGrab.grab(bbox=(0, 0, width, height))
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)  # converting in rgb color
        cv2.imshow('Screen Recorder', img_final)

        captured_video.write(img_final)  # writing video

        if cv2.waitKey(10) == ord('q'):
            break  # stops recording


# screen_recorder2()
