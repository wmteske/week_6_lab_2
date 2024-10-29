import json
from pathlib import Path

data_dir = Path.cwd() / 'data'

# Specify the path to your JSON file
file_path = data_dir / 'sample_1.json'

# Open and read the JSON file
# Load and parse the JSON file
try:
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Access and print specific fields from the JSON
    print("First Name:", data["firstName"])
    print("Age:", data["age"])
    print("Is Student:", data["isStudent"])
    print("Courses:", ", ".join(data["courses"]))
    print("City:", data["address"]["city"])
    print("Postal Code:", data["address"]["postalCode"])
    print("Spouse:", data["spouse"])

except FileNotFoundError:
    print("The JSON file was not found. Please ensure it is located in 'exercise_2/data/sample_1.json'")
