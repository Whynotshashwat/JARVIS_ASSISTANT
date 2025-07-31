import wikipedia
from utils.speak import speak
from utils.listen import listen

def search_wikipedia(command):
    speak("Searching Wikipedia...")
    try:
        for keyword in ["search wikipedia for", "search wikipedia", "in wikipedia search for", "wikipedia"]:
            if keyword in command:
                command = command.replace(keyword, "")
        topic = command.strip()
        if not topic:
            speak("What should I search on Wikipedia?")
            topic = listen()
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
    except wikipedia.exceptions.DisambiguationError:
        speak("That topic is too ambiguous.")
    except wikipedia.exceptions.PageError:
        speak("Page not found.")
    except Exception as e:
        speak("Wikipedia error.")
        print("Wikipedia error:", e)
