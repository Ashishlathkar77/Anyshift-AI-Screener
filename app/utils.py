import json
from app.schemas import ScreeningInput

def load_input_from_file(file_path: str) -> ScreeningInput:
    with open(file_path, 'r') as f:
        data = json.load(f)
    return ScreeningInput(**data)