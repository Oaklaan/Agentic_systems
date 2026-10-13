# Python Learning Assistants

A small collection of command-line assistants for learning Python. The project includes rule-based chatbots, a voice assistant, and conversational assistants powered by OpenAI or Google Gemini.

## Project contents

| File | Description |
| --- | --- |
| `simple_bot.py` | A lightweight, rule-based chatbot for basic Python topics such as variables, loops, functions, and lists. |
| `ready_to_go_bot.py` | A more feature-rich rule-based Python tutor with topic explanations, chat commands, and simple code debugging. |
| `voice-assistance.py` | A voice-driven Python tutor that listens through your microphone and reads its answers aloud. |
| `OpenAI_bot.py` | A conversational Python assistant using OpenAI through LangChain. |
| `Gemini_bot.py` | A conversational Python assistant using Google Gemini through LangChain. |
| `demo.txt` | A sample text file included with the project. |

Each assistant is a standalone script; run only the one you want to use.

## Requirements

- Python 3.10 or newer
- An internet connection for the OpenAI, Gemini, and online speech-recognition features
- A microphone and audio output device for the voice assistant

## Setup

From the project directory, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies for the assistants you plan to run:

```powershell
# OpenAI and Gemini assistants
python -m pip install langchain-core langchain-openai langchain-google-genai

# Voice assistant (optional)
python -m pip install SpeechRecognition pyttsx3 sounddevice
```

The rule-based assistants use only the Python standard library and need no additional packages.

## Run an assistant

Run a script from the project directory:

```powershell
python simple_bot.py
python ready_to_go_bot.py
python OpenAI_bot.py
python Gemini_bot.py
python voice-assistance.py
```

For the rule-based assistants, type `help` to see available commands where supported, and type `exit` to quit.

## API keys

- **OpenAI:** `OpenAI_bot.py` currently has an `api-key-here` placeholder in its `ChatOpenAI` configuration. Replace it locally with your OpenAI API key before running the script.
- **Gemini:** `Gemini_bot.py` prompts for your Google Gemini API key when it starts.

Never commit API keys or other credentials. Keep any locally edited key out of commits; if a key is accidentally exposed, revoke it with the provider and create a new one.

## Voice assistant notes

The voice assistant uses the default microphone, records short audio clips, and sends speech for recognition using Google's online speech-recognition service. It requires an internet connection and working microphone/audio drivers. If `sounddevice` cannot access the audio device, check your operating-system audio permissions and device configuration.

## Troubleshooting

- If Python or a package cannot be found, confirm the virtual environment is active and install the dependencies listed above.
- If an LLM assistant reports an authentication or API error, check that the key is valid and that the corresponding provider account has access to the configured model.
- If the voice assistant cannot hear or understand you, check the microphone input and internet connection.
