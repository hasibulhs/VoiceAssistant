from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from talk import talk


def bubt():
    service = Service(r"C:\Users\hasib\PycharmProjects\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    talk("Opening BUBT Website")
    driver.get('https://bubt.edu.bd/')
    sleep(1)

    talk("And directing you to the notice board section.")
    driver.find_element(By.XPATH, '//*[@id="ip-container"]/div[2]/div[1]/div/div/ul[2]/li[4]/a/img').click()
    sleep(30)


# bubt()
