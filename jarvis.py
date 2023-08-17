import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define Jarvis's responses
responses = {
    "hello": "Hello! How can I assist you?",
    "how are you":"I'm just a program, but I'm functioning well!",
    "what's the time": "The current time is 4:45 AM ",
    "who make you": " Ravi made me August 16 at 4:46 am",
    "anmol": "He is a kind person ",
    "list my friends": " Lasun  Anmol hippy bhaii ",
    "mummy":"MY mummy is beautiful"

    # Add more responses here
}

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""

def respond(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def main():
    respond("Hello, I'm your AI assistant. I am here for you at your service Ravi Sir ")
    
    while True:
        command = listen_for_command()
        
        if command in responses:
            respond(responses[command])
        elif "exit" in command:
            respond("Goodbye RAVI ")
            break
        else:
            respond("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
