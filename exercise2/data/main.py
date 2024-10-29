import json  # Import the built-in json module to parse and work with JSON data
import pprint  # Import pprint to pretty-print the JSON data in a readable format
from pathlib import Path  # Import Path from pathlib to handle file paths in a platform-independent way

# Set the directory where the JSON file is located
data_dir = Path.cwd() / 'data'  # Path.cwd() gives the current working directory, and 'data' is appended to it

# Specify the path to your JSON file inside the data directory
file_path = data_dir / 'sample_1.json'  # Create a full file path by combining the directory and the JSON file name

# Open the JSON file in read mode ('r') using a context manager (with statement)
with open(file_path, 'r') as file:
    data = json.load(file)  # Load JSON data from the file and convert it into a Python dictionary

# Pretty-print the contents of the JSON file for better readability
pprint.pprint(data)

# Access and store specific values from the JSON data
age = data['age']  # Extract the 'age' value from the JSON dictionary
is_student = data['isStudent']  # Extract the 'isStudent' value from the JSON dictionary
address = data['address']  # Extract the 'address' dictionary from the JSON dictionary

# Print the extracted values
print(age)  # Print the 'age' value
print(is_student)  # Print the 'isStudent' value
