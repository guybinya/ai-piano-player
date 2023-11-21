import json
from typing import Dict, Any
from pathlib import Path

file_path = r"./saved_data"


def append_json_to_file(json_obj: Dict[Any, Any]) -> None:
    # Check if the file exists
    file = Path(file_path)
    data = []
    if file.is_file():
        # Read the existing data
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                # Ensure that the data is a list
                if not isinstance(data, list):
                    raise ValueError(f"Data in {file_path} is not a list")
            except json.JSONDecodeError:
                # File is empty or not valid JSON; start with an empty list
                data = []

    # Append the new JSON object
    data.append(json_obj)

    # Write the updated data back to the file
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)


# # Example usage:
# new_data = {'key': 'value'}
# append_json_to_file(new_data, '/path/to/your/file.json')
