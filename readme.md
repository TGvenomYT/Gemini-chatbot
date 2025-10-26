# 🎙️ Speech Assistant with Google Gemini AI

[![Python](https://img.shields.io/badge/python-3.11+-blue)](https://www.python.org/)  
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Code Size](https://img.shields.io/github/languages/code-size/yourusername/speech-assistant)](https://github.com/yourusername/speech-assistant)  

A Python-based **voice assistant** that converts your speech into text, queries **Google Gemini AI**, and reads the responses back using **text-to-speech**.  

---


---

## ⚡ Features

| Feature | Description |
|---------|-------------|
| **Speech Recognition** | Converts your voice to text using `speech_recognition`. |
| **Text-to-Speech** | Speaks responses using `gTTS`. |
| **AI-Powered Responses** | Uses Google Gemini 2.5 Flash model for intelligent responses. |
| **Voice Commands** | Stop the assistant with voice commands like `exit`, `quit`, or `stop`. |
| **Cross-Platform** | Works on Windows, Linux, and MacOS (requires microphone support). |

---
** 🚀 Installation**

1. **Clone the repository**:

bash
git clone https://github.com/yourusername/speech-assistant.git
cd speech-assistant

    Create a virtual environment (optional):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

    Install dependencies:

pip install -r requirements.txt

    Set up environment variables:

Create a .env file in the project root:

OPENROUTER_API_KEY=your_openrouter_api_key_here

    Replace your_openrouter_api_key_here with your actual OpenRouter or Gemini API key.

**🎤 Usage**

Run the assistant:

python assistant.py

    Speak naturally into your microphone.

    The assistant will respond using voice.

    Say exit, quit, or stop to end the session.

**📦 Dependencies**

    requests – API communication

    speech_recognition – convert speech to text

    gTTS – Google Text-to-Speech

    playsound – play audio files

    python-dotenv – load environment variables

Install all dependencies with:

pip install requests speechrecognition gTTS playsound python-dotenv

**⚠️ Notes**

    Ensure your microphone works properly.

    The Gemini model requires a valid API key.

    Temporary audio files are deleted after playback automatically.

📄 License

This project is licensed under the MIT License.


** 💬 Connect With Me**

<p align="center">
  <a href="https://github.com/TGvenomYT">
    <img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  <a href="https://Discord.com/users/tgvenom0441">
     <img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white"/>
  </a>
  <a href="mailto:rajicbe1969@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white"/>
  </a>
</p>
