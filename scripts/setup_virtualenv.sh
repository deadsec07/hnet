#!/bin/bash

# Ensure Python 3 and virtualenv are installed
echo "Setting up a Python virtual environment..."

python3 -m venv venv
source venv/bin/activate

# Install dependencies from the requirements file
pip install -r requirements.txt

echo "Virtual environment setup complete. To activate, run 'source venv/bin/activate'."

