import speech_recognition as sr
import pyttsx3
import datetime
import os

engine = pyttsx3.init()
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio).lower()
    print("You said:", text)

    if text == "hello":
        print("Hello! How can I help you?")
        engine.say("Hello! How can I help you?")

    elif text == "time":
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print("Current Time:", current_time)
        engine.say("Current time is " + current_time)

    elif text == "date":
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print("Today's Date:", current_date)
        engine.say("Today's date is " + current_date)

    elif text == "medicine":
        print("Opening Medicine Reminder")
        engine.say("Opening Medicine Reminder")
        os.system("python reminder.py")

    elif text == "weather":
        print("Opening Weather Report")
        engine.say("Opening Weather Report")
        os.system("python weather.py")

    elif text == "sos":
        print("Emergency SOS Activated")
        engine.say("Emergency SOS Activated")
        os.system("python sos.py")

    elif text == "exit":
        print("Good Bye!")
        engine.say("Good Bye")

    else:
        print("Command Not Found!")
        engine.say("Sorry, I don't understand.")

    engine.runAndWait()

except Exception:
    print("Could not understand your voice.")