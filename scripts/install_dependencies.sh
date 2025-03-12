#!/bin/bash

# Update system and install dependencies
echo "Updating package lists..."
sudo apt update

echo "Installing required system dependencies..."
sudo apt install -y python3 python3-pip python3-venv build-essential libssl-dev libffi-dev python3-dev

# Installing common security tools
echo "Installing security tools..."
sudo apt install -y nmap tcpdump netcat ncat

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Installation complete!"

