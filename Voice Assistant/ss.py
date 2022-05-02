import pyautogui
import datetime


def ss():
    time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')  # creating dynamic file name using time
    file_name = f'{time_stamp}'  # creating dynamic file name using time
    pyautogui.screenshot('C:/Users/hasib/PycharmProjects/screenshots/ss'+file_name+'.png')


# ss()
