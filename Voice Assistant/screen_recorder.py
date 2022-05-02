import cv2 as cv2
import numpy as np
import pyautogui
import datetime


def screen_recorder():
    SCREEN_SIZE = pyautogui.size()

    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # creating dynamic file name using time
    file_name = f'{time_stamp}.avi'  # creating dynamic file name using time

    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(file_name, fourcc, 16.0, SCREEN_SIZE)

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("Screen Recorder", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    cv2.destroyAllWindows()
    out.release()


# screen_recorder()
