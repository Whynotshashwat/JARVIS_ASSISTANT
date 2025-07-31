import os
import platform
import subprocess
import webbrowser
from utils.speak import speak
from utils.listen import listen

def play_music():
    speak("What do you want me to play?")
    user_input = listen()

    if not user_input:
        speak("I didn't catch that.")
        return

    # Remove 'play' from the command
    song_name = user_input.lower().strip()
    if song_name.startswith("play "):
        song_name = song_name[5:]

    if not song_name:
        speak("You didn't mention a song.")
        return

    speak(f"Playing {song_name} on Spotify")
    search_query = song_name.replace(" ", "+")
    url = f"https://open.spotify.com/search/{search_query}"
    webbrowser.open(url)

def tell_time():
    from datetime import datetime
    now = datetime.now().strftime("%I:%M %p")
    speak(f"The time is {now}")

def open_calculator():
    speak("Opening calculator")
    try:
        if platform.system() == "Windows":
            os.system("start calc")
        elif platform.system() == "Darwin":
            os.system("open -a Calculator")
        elif platform.system() == "Linux":
            subprocess.Popen(["gnome-calculator"])
    except Exception as e:
        speak("Could not open calculator.")

def shutdown_computer():
    speak("Are you sure you want to shut down the computer?")
    response = listen()
    if response and "yes" in response.lower():
        speak("Shutting down now.")
        if platform.system() == "Windows":
            os.system("shutdown /s /t 5")
        elif platform.system() == "Linux":
            os.system("shutdown now")
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -h now")
    else:
        speak("Shutdown canceled.")
