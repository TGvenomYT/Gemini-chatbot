import os
import requests
import speech_recognition as sr
from dotenv import load_dotenv

# 1. Load environment variables
load_dotenv()
API_KEY = os.getenv('GEMINI_API_KEY')

if not API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file.")
    exit()

recognizer = sr.Recognizer()

# 2. Clean AI text for better speech
def clean_text(text):
    chars_to_remove = ["*", "_", "#", "@", "/", "<", ">", "{", "}", "[", "]", "\\", "|", "`", "~", "^"]
    for ch in chars_to_remove:
        text = text.replace(ch, "")
    return " ".join(text.split()).strip()

# 3. Native Termux Speech (No playsound needed)
def speak(text):
    try:
        text = clean_text(text)
        print(f"AI: {text}")
        # Uses Android system TTS directly
        os.system(f'termux-tts-speak "{text}"')
    except Exception as e:
        print(f"Speak Error: {e}")

# 4. Native Termux Listening (No PyAudio needed)
def listen():
    try:
        print("Listening...")
        # Record 5 seconds to a file using Android hardware
        os.system("termux-microphone-record -f input.wav -l 5")
        
        # Process the file with SpeechRecognition
        if os.path.exists("input.wav"):
            with sr.AudioFile("input.wav") as source:
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language='en-US')
            print(f"You: {text}")
            return text
    except Exception:
        return None
    finally:
        if os.path.exists("input.wav"):
            os.remove("input.wav")
    return None

# 5. Gemini API Call
def gemini_query(query):
    MODEL = "gemini-2.0-flash"
    url = f"https://generativelanguage.googleapis.com{MODEL}:generateContent"
    headers = {"Content-Type": "application/json", "x-goog-api-key": API_KEY}
    payload = {"contents": [{"role": "user", "parts": [{"text": query}]}]}
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception as e:
        return f"API Error: {e}"

# 6. Start the App
def main():
    speak("Hello! I am ready.")
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
