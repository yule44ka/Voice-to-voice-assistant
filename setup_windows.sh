#!/bin/bash

# Set up a virtual environment
python -m venv venv
source venv/Scripts/activate

# Install the required packages
pip install pyaudio
pip install -r requirements.txt
