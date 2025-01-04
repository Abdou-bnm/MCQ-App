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
#crud operations

#add new category
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
    
    # read category
    def read_category(self, name: str) -> Optional[Dict]:
        """Get a category by name"""
        data = self._load_data()
        for category in data["categories"]:
            if category["name"] == name:
                return category
        return None
# get list of categories 
    def list_categories(self) -> List[str]:
        """Get a list of all category names"""
        data = self._load_data()
        return [category["name"] for category in data["categories"]]

# update category
    def update_category(self, name: str, new_name: Optional[str] = None, 
                       new_levels: Optional[List] = None) -> bool:
        """
        Update a category's name and/or levels
        Returns True if successful, False if category not found
        """
        data = self._load_data()
        
        for category in data["categories"]:
            if category["name"].lower() == name.lower():
                if new_name:
                    category["name"] = new_name
                if new_levels:
                    category["levels"] = new_levels
                self._save_data(data)
                return True
        return False
#delete category
    def delete_category(self, name: str) -> bool:
        """
        Delete a category by name
        Returns True if successful, False if category not found
        """
        data = self._load_data()
        initial_length = len(data["categories"])
        
        data["categories"] = [cat for cat in data["categories"] if cat["name"] != name]
        
        if len(data["categories"]) < initial_length:
            self._save_data(data)
            return True
        return False


    
    
    

  