import webbrowser

def execute_command(command, speak):

    if "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://youtube.com")

    elif "google" in command:

        speak("Opening Google")

        webbrowser.open("https://google.com")

    else:

        speak("Command not recognized")