REM Set up a virtual environment
python -m venv venv
call venv\Scripts\activate

REM Install the required packages
pip install pyaudio
pip install -r requirements.txt