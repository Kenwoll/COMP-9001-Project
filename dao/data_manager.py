"""
Data Manager - Handles JSON file operations
"""


import os
import json

class DataManager:
    def __init__(self):
        self.data_dir = "data"

    def load_json(self, filename):
        """Load data from JSON file"""
        try:
            file_path = os.path.join(self.data_dir, filename)

            with open(file_path, "r") as f:
                data = json.load(f)
            return data
        except json.JSONDecodeError:
            raise Exception(f"Error: {filename} contains invalid JSON")
        except Exception as e:
            raise Exception(f"Error loading {filename}: {str(e)}")

    def save_json(self, filename, data):
        """Save data to JSON file."""
        try:
            file_path = os.path.join(self.data_dir, filename)
            with open(file_path, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            raise Exception(f"Error saving {filename}: {str(e)}")