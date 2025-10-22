import requests
import speech_recognition as sr
import os
from dotenv import load_dotenv
from gtts import gTTS
import playsound

# Load environment variables from .env file
load_dotenv()
# Get the API key from the environment variable
API_KEY = os.getenv('OPENROUTER_API_KEY')
if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found. Please set it in the .env file or environment variables.")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert text to speech using gTTS
def speak(text):
    try:
        tts = gTTS(text=text, lang='en')
        filename = "temp_speech.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove(filename)  # Remove the temporary file
    except Exception as e:
        print(f"Error during speech synthesis: {e}")

# Function to recognize speech and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

# Function to interact with OpenRouter API

import requests

def gemini_query(query):
    API_KEY = 'AIzaSyCkMHAdK8zLget-A796EqLEtGWZoAOR9XE'  # Replace with your Google AI Studio API key
    MODEL = "gemini-2.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

    headers = {
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": query}]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()

        data = response.json()
        # Safely extract the model output
        return data["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.HTTPError as e:
        return f"HTTP Error {response.status_code}: {response.text}"
    except Exception as e:
        return f"Error: {e}"




# Main function to run the assistant
def main():
    speak("Hello, I am your speech assistant. How can I assist you?")
    while True:
        query = listen()
        if query:
            if query.lower() in ["exit", "quit", "stop"]:
                speak("Goodbye!")
                break
            response = gemini_query(query)
            speak(response)

if __name__ == "__main__":
    main()
