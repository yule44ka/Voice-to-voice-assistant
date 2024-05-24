# Voice Assistant

I used OpenAI API: ChatGPT (gpt-4o) for generating, Whisper for recognizing text and TTS for translating from Text to Speech.

In addition, I implemented: 

- Add Short-term Memory - Develop short-term memory capabilities to remember the context of ongoing sessions.

It can be also used local model.

If you don't have API key for OpenAI, you can watch my video on Google Drive or write me in [Telegram](https://t.me/yule4444ka) for testing on my laptop personally.

Google Drive with recording: https://drive.google.com/drive/folders/1Dsh-AfnhQ-Ez8rKWDXl7jBhmhwl9CYTt?usp=sharing

I tried to do this homework using WSL, but it was unsuccessfully. As far as I understand, WSL can't input my voice, so I completed work using Windows CMD.

# Structure

```plaintext
voice_assistant/
├── voice_assistant/
│   ├── audio.py
│   ├── api_key_manager.py
│   ├── config.py
│   ├── transcription.py
│   ├── response_generation.py
│   ├── text_to_speech.py
│   ├── utils.py
├── .env
├── run_voice_assistant.py
├── setup_windows.sh
├── setup_linux.sh
├── requirements.txt
└── README.md
```

# Setup Instructions

There should be:

- Python 3.10 or higher
- Virtual environment venv (recommended, but if you want, you can run without venv)

1. **Clone the repository**

2. **Set up a virtual environment and install libraries**

*For Windows:*

```shell
    setup_windows.bat
```

*For Linux:*

```shell
    ./setup_linux.sh
```

4. **Set up the environment variables** 

Create a `.env` file in the root directory and add your API key:
```shell
    OPENAI_API_KEY=your_openai_api_key
    LOCAL_MODEL_PATH=path/to/local/model
```

4.   **Run the voice assistant**

```shell
   python run_voice_assistant.py
```
