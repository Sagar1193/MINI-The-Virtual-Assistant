import speech_recognition as sr  # type: ignore
import pyttsx3  # type: ignore
import pywhatkit  # type: ignore
import datetime
import pyautogui  # type: ignore

listener = sr.Recognizer()
assistant = pyttsx3.init()
voices = assistant.getProperty('voices')
assistant.setProperty('voice', voices[1].id)

def talk(text):
    assistant.say(text)
    assistant.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'mini' in command:
                command = command.replace('mini', '')
            print(command)
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""  # Return an empty string if there's an error

def run_mini():
    command = take_command()
    if not command:
        return  # Skip processing if no valid command is received
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'open google and search' in command:
        talk("Searching, please wait.")
        query = command.replace('open google and search', '')
        pywhatkit.search(query)

    elif 'open youtube and search' in command:
        talk("Searching, please wait.")
        query = command.replace('open youtube and search', '')
        pywhatkit.search(query)

    elif 'send a message' in command:
        talk("Sending message, please wait.")
        try:
            pywhatkit.sendwhatmsg("+7019050938", "hello how are you", 0, 0)
            talk("Message sent successfully!")
        except Exception as e:
            print(f"Error: {e}")
            talk("An unexpected error occurred!")

    elif 'shutdown' in command:
        pywhatkit.shutdown(time=60)
        talk("Shutting down in 60 seconds.")

    elif 'cancel' in command:
        pywhatkit.cancel_shutdown()
        talk("Shutdown operation cancelled.")

    elif 'date' in command:
        today = datetime.date.today()
        talk(f"Today's date is {today}")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f"The current time is {time}")

    elif 'take a screenshot' in command:
        talk("Taking a screenshot, please wait.")
        my_screen = pyautogui.screenshot()
        my_screen.save("my_screen.png")
        talk("Screenshot saved successfully!")

    elif 'hello' in command:
        talk("Hey, I am Mini. What can I do for you?")

    elif 'thank you' in command:
        talk("You're welcome. I'm always here for you.")

    elif 'repeat after me' in command:
        response = command.replace('repeat after me', '')
        talk(response)

    elif 'age?' in command:
        talk("I can't tell you that; it's a secret!")

    elif 'birthday?' in command:
        talk("I don't know my birthday, sorry!")

    elif 'who is your best friend' in command:
        talk("You are my best friend!")

    elif 'where are you from' in command:
        talk("I am from the future!")

    elif 'name?' in command:
        talk("I don't know your name. Tell me, and I'll remember it!")

    elif 'favour' in command:
        talk("Of course, tell me how I can help.")

    elif 'shut up' in command:
        talk("Please don't be rude to me.")

    else:
        talk("Please say the command again.")

while True:
    run_mini()
