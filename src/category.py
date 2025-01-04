import json
from typing import List, Dict, Optional, Union

class CategoryManager:
    def __init__(self, file_path: str = "questions_1.json"):
        self.file_path = file_path
    #load categories    
    def _load_data(self) -> Dict:
        """Load data from JSON file"""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"categories": []}
        except json.JSONDecodeError as e:
            raise Exception(f"Invalid JSON format: {e}")
    #save new data 
    def _save_data(self, data: Dict) -> None:
        """Save data to JSON file"""
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)

    def create_category(self, name: str, levels: Optional[List] = None) -> bool:
        """
        Create a new category with optional levels.
        
        Arguments:
        name (str): The name of the category to be created. It must be a string and is required.
        levels (Optional[List], optional): A list of dictionaries, each containing a 'level' (str) and a 'questions' (list).
                                             If not provided, the default levels ("easy", "medium", "hard") will be used.
                                             The default is None, which means the default levels will be used.

        Returns:
        bool: Returns True if the category was successfully created, False if the category already exists.
        """
        data = self._load_data()
        
        # Check if category already exists
        if any(category["name"].lower() == name.lower() for category in data["categories"]):
            return False
        
        new_category = {
            "name": name,
            "levels": levels if levels else [
                {"level": "easy", "questions": []},
                {"level": "medium", "questions": []},
                {"level": "hard", "questions": []}
            ]
        }
        
        data["categories"].append(new_category)
        self._save_data(data)
        return True

  