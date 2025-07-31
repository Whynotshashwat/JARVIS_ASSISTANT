import sys
from utils.speak import speak, speak_emotion
from utils.listen import listen
from utils.memory import get_user_name
from utils.api_usage import can_use_api
from commands.wolfram import answer_wolfram
from commands.open_sites import open_youtube, open_google, open_browser, open_website
from commands.system_control import play_music, tell_time, open_calculator, shutdown_computer
from commands.wikipedia_search import search_wikipedia
from commands.joke_alarm import tell_joke, set_alarm
from datetime import datetime
import os

# Logging
def log_command(command):
    os.makedirs("logs", exist_ok=True)
    with open("logs/command_log.txt", "a") as f:
        f.write(f"{datetime.now()} - {command}\n")

# Command Handler
def handle_command(command, user_name):
    if "change my name" in command:
        speak("Sure, what should I call you?")
        new_name = listen()
        if new_name:
            new_name = new_name.lower().replace("my name is", "").replace("name is", "").strip().title()
            with open("data/user.txt", "w") as f:
                f.write(new_name)
            speak_emotion([f"Got it! I'll call you {new_name} from now on."], "happy")
        else:
            speak_emotion(["Still couldn't catch your name. I'll stick with the current one."], "sad")

    elif "exit" in command or "stop" in command:
        speak_emotion(["Stopping now.", "See you later!", "Goodbye!"], "happy")
        sys.exit()
    elif "open youtube" in command:
        open_youtube()

    elif "play music" in command:
        play_music()

    elif "what time" in command or "tell me time" in command:
        tell_time()

    elif "open google" in command or "search google" in command:
        open_google()

    elif "open browser" in command:
        open_browser()

    elif "open calculator" in command:
        open_calculator()

    elif "shutdown" in command or "shut down" in command:
        shutdown_computer()

    elif "wikipedia" in command:
        search_wikipedia(command)

    elif "joke" in command or "tell me a joke" in command:
        tell_joke()

    elif "set alarm" in command:
        set_alarm()

    else:
        answer = answer_wolfram(command)
        if answer and answer.strip():
            speak(answer)
        else:
            speak("I couldn't find an answer. Do you want me to search on Google?")
            confirm = listen()
            if confirm and "yes" in confirm.lower():
                open_website(command)
            else:
                speak("Okay, skipping Google search.")

# Assistant Startup
def main():
    user_name = get_user_name()
    speak_emotion([
        f"Hello {user_name}, how can I help you today?",
        f"Hi {user_name}, I'm online and ready.",
        f"Hey {user_name}, Jarvis here. What can I do for you?"
    ], "happy")
    speak("Say 'Jarvis' when you need me.")

    while True:
        command = ""
        for _ in range(2):
            command = listen()
            if command: break
            speak("I didn't catch that. Want to try again?")
            retry = listen()
            if retry and "no" in retry.lower():
                speak_emotion(["Okay, shutting down. Bye!"], "sad")
                sys.exit()

        if not command.lower().startswith("jarvis"):
            continue

        command = command[6:].strip().lower()
        log_command(command)
        handle_command(command, user_name)

if __name__ == "__main__":
    main()
