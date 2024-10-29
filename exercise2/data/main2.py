import json
from pathlib import Path

data_dir = Path.cwd() / 'data'

# Specify the path to your JSON file
file_path = data_dir / 'sample_1.json'

# Open and read the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON data as a Python dictionary
