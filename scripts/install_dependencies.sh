#!/usr/bin/env bash
set -euo pipefail

echo "[hnet] Detecting platform and installing system dependencies..."

has_cmd() { command -v "$1" >/dev/null 2>&1; }

if has_cmd apt; then
  echo "[hnet] Using apt to install packages..."
  sudo apt update
  sudo apt install -y python3 python3-pip python3-venv build-essential libssl-dev libffi-dev python3-dev \
    nmap tcpdump netcat
elif has_cmd brew; then
  echo "[hnet] Using Homebrew to install packages..."
  brew update
  # python and pip are included with brew's python
  brew install python nmap libffi openssl
else
  echo "[hnet] Unsupported package manager. Please install dependencies manually: python3, pip, venv, nmap."
fi

echo "[hnet] Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r "$(git rev-parse --show-toplevel 2>/dev/null || pwd)/requirements.txt"

echo "[hnet] Installation complete."
