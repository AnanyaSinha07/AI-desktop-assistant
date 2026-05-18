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

    elif "stop" in command or "bye" in command or "goodbye" in command:

        speak("Goodbye bro")

        break

    else:

        execute_command(command, speak)