import pyttsx3

engine = pyttsx3.init()  # initializing a variable named engine
voices = engine.getProperty('voices')  # getting details of current voice
# engine.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female
engine.setProperty('rate', 140)


def talk(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


# talk("This is a test")
