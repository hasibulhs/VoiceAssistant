from __future__ import print_function

import subprocess
import warnings
import pyttsx3
import playsound
import random
import wikipedia
import webbrowser
import ctypes
import winshell
import pyjokes
import requests
import json
from twilio.rest import Client
import wolframalpha
import time
import datetime
import os.path

from talk import talk
from rec_audio import rec_audio
from response import response
from mp3 import mp3
from call import call
from today_date import today_date
from say_hello import say_hello
from google_calender import google_calender
from calender_events import calender_events
from wiki_person import wiki_person
from note import note
from send_email import send_email
from pizza import pizza
from screen_recorder import screen_recorder
from screen_recorder2 import screen_recorder2
from game import game
from ss import ss
from bubt import bubt

warnings.filterwarnings("ignore")  # for ignoring the warnings

engine = pyttsx3.init()  # initializing a variable named engine with information of the current driver
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female


"""
try:
    service = google_calender()
    calender_events(10, service)

except Exception as e:
    talk("Could not connect to the local wifi network. Please try again later !")
    exit()
"""

talk("Hey there!\nI'm your Voice Assistant, how can I help you?")
while True:  # main function
    text = rec_audio()
    text = text.lower()
    speak = " "

    if call(text):
        speak = speak + say_hello(text)

        if "how are you" in text:
            speak = speak + "I am having a good day thank you!"
            speak = speak + "\nWhat about you?"

        elif "fine" in text or "good" in text:
            speak = speak + "It's good to know that you are fine."

        elif "your name" in text:
            speak = speak + "My name is Assistant."

        elif "who are you" in text or "yourself" in text:
            speak = speak + """I'm your assistant. I am here to make your life easier. 
            You can command me to perform various task such as solving mathematical questions, opening applications, etcetera."""

        elif "why do you exist" in text or "why did you come" in text:
            speak = speak + "It is a secret."

        elif "who am i" in text:
            speak = speak + "You must probably a human."

        elif "date" in text or "day" in text or "month" in text:  # date
            get_today = today_date()
            speak = speak + " " + get_today

        elif "time" in text:  # time
            now = datetime.datetime.now()

            meridiem = ""
            if now.hour >= 12:
                meridiem = "pm"
                hour = now.hour - 12

            else:
                meridiem = "am"
                hour = now.hour

            if now.minute < 10:
                minute = "0" + str(now.minute)

            else:
                minute = str(now.minute)

            speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + "."

        elif "wikipedia" in text:  # wikipedia
            try:
                if "who is" in text:
                    person = wiki_person(text)
                    wiki = wikipedia.summary(person, sentences=1)
                    speak = speak + " " + wiki

            except Exception:
                speak = speak + "Sorry! Nothing found."

        elif "open" in text:
            if "chrome" in text:
                speak = speak + "Opening google chrome."
                os.startfile(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # to avoid error, we are using "r" as prefix
                )

            elif "word" in text:
                speak = speak + "Opening microsoft word."
                os.startfile(
                    r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"
                )

            elif "excel" in text:
                speak = speak + "Opening microsoft excel."
                os.startfile(
                    r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.exe"
                )

            elif "vs code" in text or "visual studio code" in text:
                speak = speak + "Opening visual studio code."
                os.startfile(
                    r"C:\Users\hasib\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                )

            elif "youtube" in text:
                speak = speak + "Opening youtube."
                webbrowser.open("https://youtube.com/")

            elif "google" in text:
                speak = speak + "Opening google."
                webbrowser.open("https://google.com/")

            elif "stackoverflow" in text:
                speak = speak + "Opening stack overflow."
                webbrowser.open("https://stackoverflow.com/")

            else:
                speak = speak + "Sorry! Application not available"

        elif "youtube" in text:
            ind = text.lower().split().index("youtube")
            search = text.split()[ind + 1:]
            speak = speak + "Opening" + str(search) + "on youtube."
            webbrowser.open(
                "https://youtube.com/results?search_query=" +
                "+".join(search)
            )

        elif "search" in text:
            ind = text.lower().split().index("search")
            search = text.split()[ind + 1:]
            speak = speak + "Searching" + str(search) + "on google."
            webbrowser.open(
                "https://google.com/search?q=" + "+".join(search)
            )

        elif "google" in text:
            ind = text.lower().split().index("google")
            search = text.split()[ind + 1:]
            speak = speak + "Searching" + str(search) + "on google."
            webbrowser.open(
                "https://google.com/search?q=" + "+".join(search)
            )

        elif "change background" in text or "change wallpaper" in text:
            img = r'C:\Users\hasib\PycharmProjects\Wall'
            list_img = os.listdir(img)
            imgChoice = random.choice(list_img)
            randomImg = os.path.join(img, imgChoice)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)

            speak = speak + "Background wallpaper changed successfully."

        elif "play music" in text or "play song" in text:
            talk("Here you go with music.")
            music_dir = r'C:\Users\hasib\PycharmProjects\music'
            songs = os.listdir(music_dir)
            d = random.choice(songs)
            random = os.path.join(music_dir, d)

            playsound.playsound(random)

        elif "empty recycle bin" in text:
            try:
                winshell.recycle_bin().empty(
                    confirm=True, show_progress=False, sound=True
                )

                speak = speak + "Recycle bin emptied."

            except Exception:
                speak = speak + "Recycle bin is already empty !"

        elif "note" in text or "remember this" in text:
            talk("What would you like me to note down?")
            note_text = rec_audio()
            note(note_text)

            speak = speak + "I have made a note of that."

        elif "joke" in text or "jokes" in text:
            talk("Get ready for some chuckles.")
            speak = speak + pyjokes.get_joke()

        elif "where is" in text:  # map
            try:
                ind = text.lower().split().index("is")
                location = text.split()[ind + 1:]
                url = "https://google.com/maps/place/" + "".join(location)

                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

            except Exception:
                speak = speak + "Sorry, nothing found !"

        elif "email to hasib" in text or "gmail to hasib" in text:
            try:
                talk("What should I say?")
                content = rec_audio()
                to = "hasibulhossainshajeeb@gmail.com"
                send_email(to, content)

                speak = speak + "Email has been sent successfully !"

            except Exception as e:
                print(e)
                talk("I'm not able to send this email !")

        elif "mail" in text or "email" in text or "gmail" in text:
            try:
                talk("What should I say?")
                content = rec_audio()
                talk("Whom should I send?")
                to = input("Enter the receiver's email address please: ")
                send_email(to, content)

                speak = speak + "Email has been sent successfully !"

            except Exception as e:
                print(e)
                speak = speak + "I'm not able to send this email !"

        elif "weather" in text:
            key = "55f5c17ab1b7a7ffc0d09772b38cbcd4"
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            ind = text.split().index("in")
            location = text.split()[ind + 1:]
            location = "" . join(location)  # converting list to string
            url = weather_url + "appid=" + key + "&q=" + location
            js = requests.get(url).json()

            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15  # converting to degree from kelvin
                temperature = "{:.2f}".format(temperature)
                humidity = weather["humidity"]
                desc = js["weather"][0]["description"]
                weather_response = "In " + location + ", the temperature is " + str(temperature) + " degree celsius, the humidity is " + \
                                    str(humidity) + ", and the weather description is " + str(desc) + "."

                speak = speak + weather_response

            else:
                speak = speak + "City not found !"

        elif "news" in text:
            url = ('https://newsapi.org/v2/everything?'
                    'q=Apple&'
                    'from=2022-02-22&'
                    'sortBy=popularity&'
                    'apiKey=3ba4a46a5b4d4a5e9aaf5bf462a8f9f2')

            try:
                response = requests.get(url)

            except:
                talk("Please check your connection")

            news = json.loads(response.text)
            talk("These are the latest news with title and description:\n")
            for new in news["articles"]:
                talk(str(new["title"]))
                engine.runAndWait()

                talk(str(new["description"]))
                engine.runAndWait()

        elif "send message" in text or "send a message" in text:
            account_sid = "AC3f6fa06ce9927bec2839b6166b0f81ee"
            auth_token = "5a3f9cbfb5982c3780f631f8394e1e69"
            client = Client(account_sid, auth_token)

            talk("What should I send?")
            message = client.messages.create(
                body=rec_audio(), from_="+19034027295", to="+880 1966 901950"
            )

            # print(message.sid)
            speak = speak + "Message sent successfully !"

        elif "calculate" in text:
            app_id = "E247KA-X9R8LL93QJ"
            client = wolframalpha.Client(app_id)
            ind = text.lower().split().index("calculate")
            text = text.split()[ind + 1:]
            res = client.query(" " . join(text))
            answer = next(res.results).text

            speak = speak + "The answer is " + answer + "."

        elif "what is" in text or "who is" in text:
            try:
                app_id = "E247KA-X9R8LL93QJ"
                client = wolframalpha.Client(app_id)
                ind = text.lower().split().index("is")
                text = text.split()[ind + 1:]
                res = client.query(" ".join(text))
                answer = next(res.results).text

                speak = speak + "The answer is " + answer + "."

            except:
                talk("Sorry, I don't know that !")

        elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
            talk("For how many seconds do you want me to sleep?")
            a = int(rec_audio())
            time.sleep(a)

            speak = speak + str(a) + " seconds completed. I'm at your service again!"

        elif "recording" in text or "record" in text:
            talk("Screen recording has started, press 'q' to stop.")
            screen_recorder()

        elif "pizza" in text:
            talk("Ordering a pizza.")
            pizza()

        elif "notice" in text or "bubt" in text:
            bubt()

        elif "toss a coin" in text or "flip a coin" in text:
            toss = ["head", "tail"]
            speak = speak + "It is a " + random.choice(toss) + "."

        elif "rock" in text or "paper" in text or "scissor" in text:
            talk("Tell me your move: Rock, Paper or Scissor?")

            move = rec_audio()
            move = move.lower()
            if "rock" in move:
                pmove = "rock"

            elif "paper" in move:
                pmove = "paper"

            elif "scissor" in move or "ceasor" in move or "caesar" in move:
                pmove = "scissor"

            else:
                talk("Sorry, Invalid move !")
                continue

            c = ["rock", "paper", "scissor"]
            cmove = random.choice(c)
            talk("I choose " + cmove + ".")

            game(cmove, pmove)

        elif "screenshot" in text:
            ss()
            talk("Screenshot captured !")

        elif "shutdown" in text:
            talk("Shutting down your windows")
            subprocess.call('shutdown / p /f')

        elif "thank you" in text:
            talk("Your most welcome !")

        elif "exit" in text or "quit" in text:
            talk("Alright, see you later!")
            exit()

        talk(speak)
