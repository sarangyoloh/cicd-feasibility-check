import json
import os

# Define file paths
current_file_path = "./current.json"
config_file_path = "./config.json"
output_file_path = "../output.json"

# Function to parse JSON file
def parse_json(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Error parsing {file_path}: {e}")
            return None

# Dictionary to hold final output
output_data = {
    "create": [],
    "update_code": [],
    "update_config": []
}

# Check if both files exist
if os.path.exists(current_file_path) and os.path.exists(config_file_path):
    print("Both files found. Parsing...")

    # Parse main JSON file
    main_data = parse_json(current_file_path)
    if main_data:
        output_data["create"] = main_data.get('create', [])
        output_data["update_code"] = main_data.get('update_code', [])
        output_data["update_config"] = main_data.get('update_config', [])

    # Parse config JSON file (optional if you need to include it in the output)
    config_data = parse_json(config_file_path)
    if config_data:
        output_data["config"] = config_data
else:
    print("One or both files not found.")

# Save the output JSON to a file
with open(output_file_path, 'w') as output_file:
    json.dump(output_data, output_file)

print(f"Output JSON written to {output_file_path}")
