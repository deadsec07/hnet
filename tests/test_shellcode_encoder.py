import subprocess
import sys
from pathlib import Path


def run_cmd(args):
    return subprocess.run([sys.executable] + args, capture_output=True, text=True, check=True)


def test_base64_encode_decode():
    repo = Path(__file__).resolve().parents[1]
    tool = repo / "tools" / "exploitation" / "shellcode_encoder.py"
    text = "This is a test"
    enc = run_cmd([str(tool), "encode", text, "base64"]).stdout
    encoded = enc.strip().splitlines()[-1]
    dec = run_cmd([str(tool), "decode", encoded, "base64"]).stdout
    decoded = dec.strip().splitlines()[-1]
    assert decoded == text

