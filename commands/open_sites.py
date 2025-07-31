import webbrowser
from utils.speak import speak
from selenium import webdriver
import time

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_browser():
    speak("Opening your browser")
    webbrowser.open("https://www.bing.com")

def open_website(query):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?q=" + query)
    time.sleep(10)
    driver.quit()
