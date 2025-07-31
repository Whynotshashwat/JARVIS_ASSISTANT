import speech_recognition as sr
from playsound import playsound
from utils.speak import speak, log_queue
import os

def listen():
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            speak("Listening...")
            if os.path.exists("resources/beep.mp3"):
                try:
                    playsound("resources/beep.mp3")
                except Exception as e:
                    if log_queue:
                        log_queue.put(f"[Beep Error] {e}")
            else:
                if log_queue:
                    log_queue.put("Beep file not found.")

            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=15, phrase_time_limit=7)
            query = recognizer.recognize_google(audio)

            print("You said:", query)
            if log_queue:
                log_queue.put(f"You said: {query}")
            return query

    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
        if log_queue:
            log_queue.put("Error: Wait timeout")
    except sr.UnknownValueError:
        speak("Sorry, I could not understand that.")
        if log_queue:
            log_queue.put("Error: Unknown value (unintelligible audio)")
    except sr.RequestError:
        speak("Could not connect to the speech service.")
        if log_queue:
            log_queue.put("Error: Request to speech service failed")
    except Exception as e:
        speak("Something went wrong.")
        print("Error:", type(e).__name__, "-", e)
        if log_queue:
            log_queue.put(f"Error: {type(e).__name__} - {e}")
    
    return None
