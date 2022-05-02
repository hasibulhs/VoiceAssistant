import speech_recognition as sr


def rec_audio():  # for recording audio
    recog = sr.Recognizer()

    with sr.Microphone() as source:
        recog.energy_threshold = 10000  # increase the spectrum of our voice, which means captures the low voices too
        recog.adjust_for_ambient_noise(source, 1.2)  # eliminates the noises around us
        print("Listening...")
        audio = recog.listen(source)

    data = " "  # for using google recognition
    try:
        data = recog.recognize_google(audio)  # sending the audio to google api who is converting it to text
        print("You said: " + data)

    except sr.UnknownValueError:
        print("Assistant could not understand the audio")

    except sr.RequestError as ex:
        print("Request error from Google Speech Recognition" + ex)

    return data


# rec_audio()
