import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class music():
    def __init__(self):
        service = Service(r"C:\Users\hasib\PycharmProjects\chromedriver.exe")
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def play(self, query):
        self.query = query
        # self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        webbrowser.open(
            "https://youtube.com/results?search_query=" +
            "+".join(query)
        )
        self.driver.find_element(By.XPATH, '//*[@id="video-title"]/yt-formatted-string').click()
        sleep(1)


# assist = music()
# assist.play('dynamite by bys')
