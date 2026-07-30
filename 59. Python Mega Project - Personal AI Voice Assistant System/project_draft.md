# JARVIS AI Voice Assistant System — Project Draft

---

## 1. Project Overview

**Project Name:** JARVIS AI Voice Assistant System  
**Author:** Bappy  
**Type:** Desktop AI Voice Assistant + Web-Based Multilingual AI Assistant  
**Language:** Python 3.x  
**Status:** Active Development  

The JARVIS AI Voice Assistant System is an intelligent, voice-controlled personal assistant inspired by the iconic JARVIS from Iron Man. The project consists of **two independent modules** that demonstrate different approaches to building AI-powered voice assistants:

1. **JARVIS CLI Voice Assistant** — A command-line voice assistant that listens to spoken commands and performs tasks like opening applications, playing music, searching Wikipedia, and more.
2. **Multilingual AI Assistant** — A web-based assistant powered by Google Gemini AI with a Streamlit frontend, capable of understanding natural language queries and responding with AI-generated answers in both text and audio.

---

## 2. Objectives

- Build a fully functional voice-controlled personal assistant using Python.
- Demonstrate speech-to-text and text-to-speech capabilities using industry-standard libraries.
- Integrate external AI (Google Gemini) for intelligent, context-aware responses.
- Provide a user-friendly web interface via Streamlit for broader accessibility.
- Implement structured logging for debugging and monitoring.
- Showcase modular Python project design across CLI and web paradigms.

---

## 3. Technology Stack

| Category               | Technology / Library                          | Purpose                                      |
|------------------------|-----------------------------------------------|----------------------------------------------|
| **Language**           | Python 3.x                                    | Core programming language                    |
| **Speech Recognition** | SpeechRecognition, PyAudio                    | Capture and transcribe voice input           |
| **Text-to-Speech**    | pyttsx3 (SAPI5)                               | Offline TTS for CLI module                   |
| **Text-to-Speech**    | gTTS (Google Text-to-Speech)                  | Online TTS for web module                    |
| **AI / LLM**          | Google Generative AI (Gemini 2.5 Flash)       | Natural language understanding & generation  |
| **Web Framework**     | Streamlit                                     | Web UI for Multilingual Assistant            |
| **Knowledge Base**    | Wikipedia API                                 | Factual information retrieval                |
| **Web Automation**    | webbrowser (stdlib)                           | Open URLs in the default browser             |
| **System Control**    | subprocess, os (stdlib)                       | Launch system applications and manage files  |
| **Logging**           | logging (stdlib)                              | Application-level logging                    |
| **Randomization**     | random (stdlib)                               | Random song selection and joke delivery      |

---

## 4. Project Structure

```
JARVIS-System/
│
├── main.py                         # Module 1: JARVIS CLI Voice Assistant
├── requirements.txt                # Dependencies for Module 1
├── architecture.jpg                # System architecture diagram
├── music/                          # Local music files for playback
├── logs/                           # Application log files
│   └── application.log
│
└── Multilingual AI Assistant/      # Module 2: Web-based AI Assistant
    ├── main.py                     # Streamlit app with Gemini integration
    ├── requirements.txt            # Dependencies for Module 2
    ├── speech.mp3                  # Generated TTS audio output
    └── logs/                       # Application log files
        └── application.log
```

---

## 5. Module Details

### 5.1 Module 1 — JARVIS CLI Voice Assistant

**Entry Point:** `main.py` (root)  
**Interface:** Command-line (terminal)  
**Voice Engine:** pyttsx3 with SAPI5 (Windows male voice)

#### Features & Command Handlers

| Command Trigger            | Action                                              |
|----------------------------|------------------------------------------------------|
| `"time"`                   | Announces the current system time                    |
| `"name"`                   | Introduces itself as JARVIS                          |
| `"how are you"`            | Responds with a status message                       |
| `"who made you"`           | Credits the creator (Bappy)                          |
| `"thank you"`              | Responds politely                                    |
| `"play music"` / `"music"` | Plays a random song from the local `music/` folder   |
| `"open calculator"`        | Launches Windows Calculator (`calc.exe`)             |
| `"open notepad"`           | Launches Windows Notepad (`notepad.exe`)             |
| `"open terminal"` / `"open cmd"` | Launches Windows Command Prompt (`cmd.exe`)    |
| `"open google"`            | Opens Google in the default browser                  |
| `"open facebook"`          | Opens Facebook in the default browser                |
| `"youtube"`                | Searches YouTube for the spoken query                |
| `"open calendar"`          | Opens Google Calendar in the browser                 |
| `"joke"`                   | Tells a random programming joke                      |
| `"wikipedia"`              | Searches Wikipedia and reads a 2-sentence summary    |
| `"exit"`                   | Says goodbye and terminates the application          |

#### Execution Flow

1. Application starts → `wish_me()` greets the user based on the time of day.
2. Enters an infinite loop → Listens for voice commands via `takeCommand()`.
3. Matches the command to a handler → Executes the corresponding action.
4. Responds via `speak()` (pyttsx3 text-to-speech).
5. Repeats until the user says `"exit"`.

---

### 5.2 Module 2 — Multilingual AI Assistant

**Entry Point:** `Multilingual AI Assistant/main.py`  
**Interface:** Web browser (Streamlit)  
**AI Engine:** Google Gemini 2.5 Flash  
**Voice Engine:** gTTS (Google Text-to-Speech)

#### Features

- **Voice Input:** Captures user speech via microphone using SpeechRecognition.
- **AI-Powered Responses:** Sends the transcribed text to Google Gemini for intelligent, natural language responses.
- **Text Display:** Shows the AI-generated response in a scrollable text area.
- **Audio Playback:** Converts the response to speech (MP3) and plays it in the browser.
- **Audio Download:** Provides a download button for the generated speech file.

#### Execution Flow

1. User opens the Streamlit web app in a browser.
2. Clicks the **"Ask me anything!"** button.
3. The app listens for voice input via the microphone.
4. Transcribed text is sent to Google Gemini 2.5 Flash for processing.
5. The AI response is displayed as text and converted to audio via gTTS.
6. Audio is played in-browser with an option to download the MP3 file.

---

## 6. Prerequisites

### System Requirements

- **OS:** Windows 10/11 (SAPI5 required for Module 1)
- **Python:** 3.8 or higher
- **Hardware:** Microphone for voice input, speakers for audio output
- **Internet:** Required for Google Speech API, Wikipedia, Gemini AI, and gTTS

### Software Dependencies

**Module 1 (`requirements.txt`):**
```
SpeechRecognition
pyttsx3==2.90
pyaudio
wikipedia
```

**Module 2 (`Multilingual AI Assistant/requirements.txt`):**
```
SpeechRecognition
pyaudio
google-generativeai
gTTS
pipwin
streamlit
```

---

## 7. Installation & Setup

```bash
# Step 1: Clone the repository
git clone <repository-url>
cd JARVIS-System

# Step 2: Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate

# Step 3: Install dependencies for Module 1
pip install -r requirements.txt

# Step 4: Run Module 1 — JARVIS CLI Assistant
python main.py

# Step 5: Install dependencies for Module 2
pip install -r "Multilingual AI Assistant/requirements.txt"

# Step 6: Run Module 2 — Multilingual AI Assistant
streamlit run "Multilingual AI Assistant/main.py"
```

> **Note:** You need a valid Google Gemini API key configured in the Module 2 source code for AI responses to work.

---

## 8. Logging

Both modules implement structured logging using Python's built-in `logging` module:

- **Log Directory:** `logs/`
- **Log File:** `application.log`
- **Format:** `[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s`
- **Level:** `INFO`

Logs capture speech recognition errors, exceptions, and application events for debugging and monitoring.

---

## 9. Key Learning Outcomes

- **Speech Recognition:** Converting spoken language to text using Google Speech API.
- **Text-to-Speech:** Converting text responses to spoken audio (pyttsx3 offline, gTTS online).
- **AI Integration:** Leveraging Google Gemini LLM for intelligent conversational responses.
- **Web App Development:** Building interactive web interfaces with Streamlit.
- **System Automation:** Controlling OS-level applications via subprocess.
- **API Integration:** Working with Wikipedia and Google APIs.
- **Logging & Debugging:** Implementing structured application logging.
- **Modular Design:** Organizing a project into independent, self-contained modules.

---

## 10. Future Enhancements

| Enhancement                          | Description                                                   |
|--------------------------------------|---------------------------------------------------------------|
| **Multi-language Support**           | Extend voice recognition and TTS to support multiple languages|
| **Wake Word Detection**              | Add "Hey JARVIS" wake word using Porcupine or Snowboy         |
| **GUI Interface**                    | Build a desktop GUI using Tkinter or PyQt                     |
| **Smart Home Integration**           | Control IoT devices via MQTT or Home Assistant API            |
| **Conversation Memory**             | Add context-aware multi-turn conversations with Gemini        |
| **Task Scheduling**                  | Integrate reminders and scheduled tasks                       |
| **Email & Messaging**               | Send emails and messages via voice commands                   |
| **Weather Updates**                  | Integrate a weather API for real-time forecasts               |
| **Secure API Key Management**        | Use environment variables or a `.env` file for API keys       |
| **Unit Testing**                     | Add comprehensive test coverage with pytest                   |

---

## 11. Deliverables

- [x] Fully functional CLI voice assistant (`main.py`)
- [x] Web-based multilingual AI assistant (Streamlit + Gemini)
- [x] Speech recognition and text-to-speech integration
- [x] Wikipedia search capability
- [x] System application launcher
- [x] Local music player
- [x] Structured logging
- [x] Architecture diagram (`architecture.jpg`)
- [x] Project documentation (`project_draft.md`)

---

## 12. References

| Resource                            | URL                                              |
|-------------------------------------|--------------------------------------------------|
| SpeechRecognition Docs              | https://pypi.org/project/SpeechRecognition/      |
| pyttsx3 Docs                        | https://pypi.org/project/pyttsx3/                |
| gTTS Docs                           | https://pypi.org/project/gTTS/                   |
| Google Generative AI (Gemini)       | https://ai.google.dev/                           |
| Streamlit Documentation             | https://docs.streamlit.io/                       |
| Wikipedia API                       | https://pypi.org/project/wikipedia/              |
| Python Logging                      | https://docs.python.org/3/library/logging.html   |

---

*Project Draft prepared for the JARVIS AI Voice Assistant System by Bappy.*
