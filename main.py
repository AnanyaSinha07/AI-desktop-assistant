from assistant.utils import get_time, get_date
from assistant.speak import speak
from assistant.listen import take_command
from assistant.commands import execute_command

speak("Hello Ananya. Your AI desktop assistant is now active.")

while True:

    command = take_command()

    if command == "":
        continue

    print(command)

    if "hello" in command:

        speak("Hello bro, how are you")

    elif "your name" in command:

        speak("I am your AI desktop assistant")
    elif "time" in command:

        current_time = get_time()

        speak(f"The time is {current_time}")

    elif "date" in command:

        current_date = get_date()

        speak(f"Today's date is {current_date}")

    elif "stop" in command or "bye" in command or "goodbye" in command:

        speak("Goodbye bro")

        break

    else:

        execute_command(command, speak)