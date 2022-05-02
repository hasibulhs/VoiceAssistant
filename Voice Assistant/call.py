def call(text):
    action_call = "assistant"
    text = text.lower()

    if action_call in text:
        return True

    return False
