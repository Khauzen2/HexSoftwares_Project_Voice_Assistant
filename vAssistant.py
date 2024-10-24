# This is my Voice Assistant Project using speech_rec, pyttsx3, webbrowser, os, and datetime modules and more...

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen for user commands
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
            return ""

# Main loop for the voice assistant
def run_assistant():
    speak("Hello, how can I assist you?")
    
    while True:
        command = listen()
        
        if 'open youtube' in command:
            speak("Opening YouTube.")
            webbrowser.open("https://www.youtube.com")
        
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif 'mike' in command:
            speak('Khauzen is a Pioneer, the best at what he does, of which it is Software Development...For more about Khauzen, please visit Orange Farm')
            
        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

        # Add more commands as you like!
        else:
            speak("I don't understand that command. Please try again.")

# Run the assistant
if __name__ == "__main__":
    run_assistant()
