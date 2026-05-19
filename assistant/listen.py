import speech_recognition as sr

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.pause_threshold = 1.5

        audio = recognizer.listen(
            source,
            phrase_time_limit=7
        )

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(
            audio,
            language="en-IN"
        )

        print(f"You said: {command}")

        return command.lower()

    except Exception:

        print("Could not understand.")

        return ""