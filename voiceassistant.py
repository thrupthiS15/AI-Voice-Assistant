import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyjokes

# Initialize voice engine
engine = pyttsx3.init()

# Voice speed
engine.setProperty('rate', 170)

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Greeting
def wish():
    hour = datetime.datetime.now().hour

    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am your voice assistant")

# Take microphone input
def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language='en-in')
        print("You said:", command)
        return command.lower()

    except Exception:
        speak("Please say that again")
        return ""

# Main function
def run_assistant():
    wish()

    while True:
        command = take_command()

        # Wikipedia search
        if 'wikipedia' in command:
            speak("Searching Wikipedia")
            command = command.replace("wikipedia", "")

            try:
                result = wikipedia.summary(command, sentences=2)
                speak(result)

            except:
                speak("No result found")

        # Open YouTube
        elif 'open youtube' in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        # Open Google
        elif 'open google' in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        # Time
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"The time is {current_time}")

        # Joke
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            speak(joke)

        # Exit
        elif 'exit' in command or 'bye' in command:
            speak("Goodbye")
            break

        else:
            speak("Command not recognized")

# Start assistant
run_assistant()