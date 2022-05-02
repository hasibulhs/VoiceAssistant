import random


def say_hello(text):  # for greeting
    greet = ["hi", "hey", "greetins", "wassup", "hello", "howdy", "what's up", "hey there"]
    response = ["hi", "hey", "greetins", "hello", "howdy", "hey there"]

    for word in text.split():
        if word.lower() in greet:
            return random.choice(response)

    return ""  # returning empty string if no greeting is detected
