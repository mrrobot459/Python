import speech_recognition as sr
import webbrowser as wb
import pyttsx3
import music  # ✅ Your custom music file

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Predefined responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you": "I'm just a program, but I'm functioning well!",
    "what's the time": "The current time is 4:45 AM",  # (Optional: Add dynamic time)
    "who make you": "Ravi made me on August 16 at 4:46 AM.",
    "anmol": "He is a kind person.",
    "friends": "Lasun, Anmol, and Hippy Bhaii.",
    "mummy": "My mummy is beautiful."
}

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except Exception as e:
        print(f"Recognition error: {e}")
        return ""

def processCommand(command):
    command = command.lower()

    # Predefined conversation responses
    if command in responses:
        speak(responses[command])

    # Exit command
    elif "exit" in command or "quit" in command:
        speak("Goodbye Ravi.")
        exit()

    # Web browsing
    elif command == "open google":
        wb.open("https://google.com")
        speak("Opening Google")
    elif command == "open youtube":
        wb.open("https://youtube.com")
        speak("Opening YouTube")
    elif command == "open facebook":
        wb.open("https://facebook.com")
        speak("Opening Facebook")
    elif command == "open linkedin":
        wb.open("https://linkedin.com")
        speak("Opening LinkedIn")

    # Music playback
    elif command.startswith("play"):
        try:
            song = command.split(" ", 1)[1]
            link = music.music.get(song.lower())
            if link:
                wb.open(link)
                speak(f"Playing {song}")
            else:
                speak(f"Sorry, I couldn't find the song {song}")
        except IndexError:
            speak("Please say the name of the song after 'play'")

    else:
        speak("I'm sorry, I don't understand that command.")

def main():
    speak("Initializing Jarvis... I am here for you, Ravi Sir.")

    while True:
        command = listen()
        if command:
            if command == "jarvis":
                speak("Hi, how can I help you?")
            else:
                processCommand(command)

if __name__ == "__main__":
    main()
