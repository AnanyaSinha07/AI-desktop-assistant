import webbrowser
import os
import wikipediaapi

def execute_command(command, speak):

    command = command.lower()

    # Websites

    if "youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    elif "google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    # Applications

    elif "calculator" in command:

        speak("Opening Calculator")

        os.system("calc")

    elif "notepad" in command:

        speak("Opening Notepad")

        os.system("notepad")

    elif "chrome" in command:

        speak("Opening Chrome")

        os.system("start chrome")

    # Wikipedia Search

        # Wikipedia Search

    elif "who is" in command or "what is" in command:

        speak("Searching Wikipedia")

        query = command.replace("who is", "")
        query = query.replace("what is", "")
        query = query.strip()

        try:

            wiki = wikipediaapi.Wikipedia(
                language='en',
                user_agent='AI Desktop Assistant'
            )

            page = wiki.page(query)

            if page.exists():

                sentences = page.summary.split(". ")
                result = ". ".join(sentences[:2])

                print(result)

                speak(result)

            else:

                speak("Sorry bro, page not found")

        except Exception as e:

            print(e)

            speak("Something went wrong")

    else:

        speak("Command not recognized")