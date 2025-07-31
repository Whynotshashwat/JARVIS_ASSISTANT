from gtts import gTTS
from playsound import playsound
import os
import random
log_queue = None
def speak(text):
    print("Assistant:", text)
    try:
        tts = gTTS(text=text, lang='en')
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except Exception as e:
        print("speech error:", e)

def speak_emotion(options, emotion="neutral"):
    message = random.choice(options)
    print("Assistant:", message)  
    speak(message)