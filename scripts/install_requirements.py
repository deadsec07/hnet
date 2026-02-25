import subprocess
import sys
from pathlib import Path

def install_requirements():
    try:
        root = Path(__file__).resolve().parents[1]
        req = root / "requirements.txt"
        print(f"Installing requirements from {req}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(req)])
        print("Requirements installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during installation: {e}")

if __name__ == "__main__":
    install_requirements()
