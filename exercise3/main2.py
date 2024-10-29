import json
from pathlib import Path

# Define the directory and file paths
data_dir = Path.cwd() / 'exercise_3' / 'data'
input_file = data_dir / 'sample_2.json'
output_file = data_dir / 'contact.json'

# Step 1: Read and Parse JSON
try:
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Step 2: Extract Contact Information
    contact_info = {
        "phone": data["patient"]["contactInfo"]["phone"],
        "email": data["patient"]["contactInfo"]["email"],
        "address": data["patient"]["contactInfo"]["address"]
    }

    # Step 3: Save to contact.json
    with open(output_file, 'w') as file:
        json.dump(contact_info, file, indent=4)

    print("Contact information saved to contact.json")

except FileNotFoundError:
    print("The input JSON file was not found.")
