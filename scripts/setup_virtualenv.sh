#!/usr/bin/env bash
set -euo pipefail

echo "[hnet] Creating Python virtual environment in ./venv ..."
python3 -m venv venv

echo "[hnet] Activating venv and installing dependencies..."
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r "$(git rev-parse --show-toplevel 2>/dev/null || pwd)/requirements.txt"

echo "[hnet] Virtual environment ready. Activate with: source venv/bin/activate"
