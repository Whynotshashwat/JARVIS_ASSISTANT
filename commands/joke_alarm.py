from utils.speak import speak
from utils.listen import listen
import pyjokes
from datetime import datetime
import time

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def set_alarm():
    speak("Tell the alarm time in HH:MM format.")
    time_input = listen()
    if not time_input:
        speak("No input. Cancelling alarm.")
        return
    try:
        speak(f"Alarm set for {time_input}")
        while True:
            current_time = datetime.now().strftime("%H:%M")
            if current_time == time_input:
                speak("Wake up! This is your alarm.")
                break
            time.sleep(20)
    except Exception as e:
        speak("Failed to set alarm.")
        print("Alarm error:", e)
