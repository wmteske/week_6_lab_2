import json
from pathlib import Path

# Sample Python dictionary (this will be converted to JSON)
data = {
    "name": "John",
    "age": 30,
    "isStudent": False,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "postalCode": "10001"
    }
}
# Set the directory where the JSON file will be saved
data_dir = Path.cwd() / 'data'

# Specify the file path where you want to write the JSON data
file_path = data_dir / 'output.json'

# Open the file in write mode ('w')
with open(file_path, 'w', encoding='utf8') as file:
    # Use json.dump() to write the Python dictionary to the file as JSON
    json.dump(data, file, indent=4)  # 'indent=4' makes the JSON output more readable (pretty-printing)

print(f"Data written to {file_path}")
