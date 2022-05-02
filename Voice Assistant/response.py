from gtts import gTTS
import playsound
import os


def response(text):
    print(text)

    tts = gTTS(text=text, lang="en")  # converting text to speech
    audio = "Audio.mp3"
    tts.save(audio)

    playsound.playsound(audio)  # playing the audio
    os.remove(audio)  # deleting that file

# response("Hello google")
