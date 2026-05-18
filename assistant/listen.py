import speech_recognition as sr

def take_command():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:

        print("\nListening...")

        # reduce background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        # listening time
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        print("You said:", command)

        return command.lower()

    except sr.UnknownValueError:

        print("Could not understand audio.")

        return ""

    except sr.RequestError:

        print("Internet connection issue.")

        return ""