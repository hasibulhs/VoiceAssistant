from selenium.webdriver.chrome.service import Service
import speech_recognition as sr
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from talk import talk
from rec_audio import rec_audio


def pizza():
    service = Service(r"C:\Users\hasib\PycharmProjects\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    talk("Opening Pizza Hut BD")
    driver.get('https://www.pizzahutbd.com/')
    sleep(1)

    talk("Finding your location")
    driver.find_element(By.XPATH, '//*[@id="delivery"]/div/div/div/span').click()
    sleep(1)

    driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[1]/a').click()
    talk("Ordering your favourite Beef Pepperoni pizza")
    driver.find_element(By.XPATH, '//*[@id="productList"]/div[15]/form/div/div[2]/div[5]/button/span').click()
    sleep(1)

    talk("Would you like to increase the quantity of the pizza?")
    qty = rec_audio()
    qty_pizza = 0
    if "yes" in qty:
        talk("How many pizzas would you like to add?")
        try:
            qty_piz = rec_audio()
            qty_pizza = int(qty_piz)
            # print(qty_pizza)
            if qty_pizza > 0:
                talk_piz = f"Adding {qty_pizza} more pizzas"
                talk(talk_piz)
                for i in range(qty_pizza):
                    driver.find_element(By.XPATH, '//*[@id="cartDetails"]/div[2]/table/tbody/tr/td[3]/span/div[3]/form/button/i').click()
                    sleep(1)
                    # print(i)

        except sr.UnknownValueError:
            talk("I don't know that!")

    else:
        pass

    talk("Would you like anything to drink?")
    qty_pepsi = 0
    qty = rec_audio()
    if "yes" in qty:
        driver.find_element(By.XPATH, '//*[@id="navbar"]/ul/li[5]/a').click()
        sleep(1)

        talk("Adding one 600 ml pepsi in your cart")
        driver.find_element(By.XPATH, '//*[@id="productList"]/div[2]/form/div/div[2]/div[4]/button').click()
        sleep(1)

        talk("Would you like to increase the quantity of the pepsi?")
        qty = rec_audio()
        if "yes" in qty:
            talk("How many pepsis would you like to add?")
            try:
                qty_pep = rec_audio()
                qty_pepsi = int(qty_pep)
                # print(qty_pepsi)
                if qty_pepsi > 0:
                    talk_pep = f"Adding {qty_pepsi} more pepsis"
                    talk(talk_pep)
                    for i in range(qty_pepsi):
                        driver.find_element(By.XPATH,
                                            '//*[@id="cartDetails"]/div[2]/table[2]/tbody/tr/td[3]/span/div[3]/form/button/i').click()
                        sleep(1)
                        # print(i)

            except sr.UnknownValueError:
                talk("I don't know that!")

        else:
            pass
    else:
        pass

    total_pizza = qty_pizza + 1
    if qty_pepsi > 0:
        total_pepsi = qty_pepsi + 1
        tell_num = f"This is your list of orders. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        talk(tell_num)
        chk_order = rec_audio()

    else:
        tell_num = f"This is your list of orders. {total_pizza} Pizzas. Do you want to checkout?"
        talk(tell_num)
        chk_order = rec_audio()

    if "yes" in chk_order:
        talk("Checking out")
        driver.find_element(By.XPATH, '//*[@id="ckt_btn"]').click()
        sleep(1)

    else:
        exit()

    phone_num = "01966901950"
    driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/input').send_keys(phone_num)
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/div/div/div/div[1]/div[2]/div/div/div/form/div[2]/div[2]/button').click()
    sleep(1)

    try:
        talk("What is your OTP?")
        sleep(1)
        otp = int(input("OTP: "))
        print(otp)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/form/input[2]').send_keys(otp)
        sleep(1)
        driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/form/div[2]/button').click()
        sleep(1)

    except sr.UnknownValueError:
        talk("Your OTP is incorrect!")

    name = "Hasibul Hossain Shajeeb"
    driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(name)
    sleep(1)

    email = "hasibulhossainshajeeb@gmail.com"
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    sleep(1)

    details = "None"
    driver.find_element(By.XPATH, '//*[@id="addressDetails"]').send_keys(details)
    sleep(1)

    additional = "None"
    driver.find_element(By.XPATH, '//*[@id="additional_information"]').send_keys(additional)
    sleep(1)

    total = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/form/div/div/div/div[4]/div[2]/div/div[1]/div/span')
    total_price = f'The total bill will be {total.text}'
    talk(total_price)
    sleep(1)

    talk("Do you want to place your order?")
    order = rec_audio()
    if "yes" in order:
        talk("placing your order")
        driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div/div[2]/form/div/div/div/div[6]/div[2]/button/span').click()
        talk("Your order has been placed successfully, Please wait and enjoy")
        sleep(2)

    else:
        talk("Oops, may be later !")
        exit()

    return None
