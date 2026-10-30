"""Given - what the container runs:  uvicorn serve:app --host 0.0.0.0 --port 8000"""

from pathlib import Path

from service import load_service

app = load_service(Path(__file__).parent / "bundle")
