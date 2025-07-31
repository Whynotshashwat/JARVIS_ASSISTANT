import os
from utils.speak import speak, speak_emotion
from utils.listen import listen

def get_user_name():
    if os.path.exists("data/user.txt"):
        with open("data/user.txt") as f:
            name = f.read().strip()
            speak_emotion([f"Welcome back, {name}!"], "happy")
            return name
    else:
        speak("Hi, I'm Jarvis. What should I call you?")
        name = listen()
        if name:
            name = name.lower().replace("my name is", "").replace("name is", "").strip().title()
            with open("data/user.txt", "w") as f:
                f.write(name)
            speak_emotion([f"Nice to meet you, {name}!"], "happy")
            return name
        else:
            speak("I'll just call you boss for now.")
            return "Boss"
