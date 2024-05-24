#!/bin/bash

# Set up a virtual environment
python -m venv venv
source venv/bin/activate

# Install the required packages
sudo apt-get update
sudo apt-get install -y portaudio19-dev
pip install -r requirements.txt