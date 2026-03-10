A simple voice-controlled personal assistant built using Python that can listen to voice commands, respond using text-to-speech, and perform tasks like opening websites and telling the current time. The assistant demonstrates how speech recognition, automation, and AI APIs can be used to build an interactive system.

This project is a beginner-friendly implementation of a voice assistant similar to Siri, Google Assistant, or Alexa, designed for learning Python automation and AI integration.

🚀 Features

🎤 Voice command recognition

🔊 Text-to-speech responses

🌐 Open popular websites using voice commands

⏰ Tell the current system time

🤖 Basic OpenAI API integration

🧠 Ambient noise adjustment for better speech recognition

🛠️ Technologies Used

Python

SpeechRecognition

pyttsx3 (Text-to-Speech)

OpenAI API

Webbrowser module

Datetime module

📂 Project Structure
Voice-Personal-Assistant
│
├── Main.py          # Main assistant logic
├── OpenAITest.py    # OpenAI API integration example
└── README.md
⚙️ Installation
1️⃣ Clone the repository
2️⃣ Install required libraries
pip install SpeechRecognition pyttsx3 openai pyaudio
3️⃣ Run the program
python Main.py
🎤 Example Voice Commands

You can speak commands like:

Open YouTube

Open Google

Open WhatsApp

Open Instagram

What is the time

The assistant will recognize your voice and perform the requested task.

🧠 How It Works

The program listens through the microphone.

Speech is converted into text using Google Speech Recognition.

The command is processed and matched with predefined actions.

The assistant responds using text-to-speech.

🔮 Future Improvements

Add AI conversation capabilities

Control system applications

Add weather and news updates

Automate daily tasks

Add more voice commands

Build a GUI interface

👨‍💻 Author

Piyush Rai
MCA Student | Python Developer | AI Enthusiast
