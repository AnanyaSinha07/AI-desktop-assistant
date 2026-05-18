import pyttsx3

engine = pyttsx3.init("sapi5")

engine.say("Hello bro. Voice test successful.")

engine.runAndWait()