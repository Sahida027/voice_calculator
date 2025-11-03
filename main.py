# main.py

import speech_recognition as sr
import pyttsx3
import re

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_audio():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        speak("Please say your calculation.")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("🗣 You said:", text)
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""

def parse_expression(text):
    # Replace common math words with operators
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("times", "*")
    text = text.replace("multiplied by", "*")
    text = text.replace("divided by", "/")
    text = text.replace("over", "/")

    # Keep only numbers and operators
    expression = re.sub(r"[^0-9\+\-\*/\.]", "", text)
    return expression

def calculate(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Error"

def main():
    speak("Welcome to the voice calculator!")
    text = get_audio()
    if text:
        expression = parse_expression(text)
        print("🔍 Parsed:", expression)
        result = calculate(expression)
        print("✅ Result:", result)
        speak(f"The result is {result}")

if __name__ == "__main__":
    main()