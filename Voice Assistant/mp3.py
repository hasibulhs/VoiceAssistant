from gtts import gTTS
import playsound
import os


def mp3(text):
    print(text)

    tts = gTTS(text)
    tts.save('hello.mp3')

    playsound.playsound('hello.mp3')
    os.remove('hello.mp3')


# mp3("Hello world")
