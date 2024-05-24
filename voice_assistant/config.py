import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


class Config:
    """
    Configuration class to hold the model selection and API keys.

    Attributes:
    TRANSCRIPTION_MODEL (str): The model to use for transcription ('openai', 'local').
    RESPONSE_MODEL (str): The model to use for response generation ('openai', 'local').
    TTS_MODEL (str): The model to use for text-to-speech ('openai', 'local').
    OPENAI_API_KEY (str): API key for OpenAI services.
    LOCAL_MODEL_PATH (str): Path to the local model.
    """
    # Model selection
    TRANSCRIPTION_MODEL = 'openai'  # possible values: openai, local
    RESPONSE_MODEL = 'openai'  # possible values: openai, local
    TTS_MODEL = 'openai'  # possible values: openai, local

    # API keys and paths
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    LOCAL_MODEL_PATH = os.getenv("LOCAL_MODEL_PATH")

    @staticmethod
    def validate_config():
        """
        Validate the configuration to ensure all necessary environment variables are set.

        Raises:
        ValueError: If a required environment variable is not set.
        """
        if Config.TRANSCRIPTION_MODEL not in ['openai', 'local']:
            raise ValueError("Invalid TRANSCRIPTION_MODEL. Must be one of ['openai', 'local']")
        if Config.RESPONSE_MODEL not in ['openai', 'local']:
            raise ValueError("Invalid RESPONSE_MODEL. Must be one of ['openai', 'local']")
        if Config.TTS_MODEL not in ['openai', 'local']:
            raise ValueError("Invalid TTS_MODEL. Must be one of ['openai', 'local']")

        if Config.TRANSCRIPTION_MODEL == 'openai' and not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI models")
        if Config.RESPONSE_MODEL == 'openai' and not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI models")
        if Config.TTS_MODEL == 'openai' and not Config.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is required for OpenAI models")
