import time
from category import CategoryManager
import os

manager = CategoryManager("./questions_1_copy.json")

def create_category_demo():
    categories_to_create = ["Math", "Science", "History", "Literature", "Technology"]
    for category in categories_to_create:
        print(f"Creating '{category}' category...")
        created = manager.create_category(category)
        print(f"Category '{category}' created: {created}")
        time.sleep(2)

    categories = manager.list_categories()
    print("Categories after creation:", categories)
    time.sleep(2)

def update_category_demo():
    updates = [("Math", "Advanced Math"), ("History", "World History")]
    for old_name, new_name in updates:
        print(f"Updating '{old_name}' category to '{new_name}'...")
        updated = manager.update_category(old_name, new_name=new_name)
        print(f"Category updated from '{old_name}' to '{new_name}': {updated}")
        time.sleep(2)

    categories = manager.list_categories()
    print("Categories after update:", categories)
    time.sleep(2)

def delete_category_demo():
    categories_to_delete = ["Advanced Math", "Literature", "Technology"]
    for category in categories_to_delete:
        print(f"Deleting '{category}' category...")
        deleted = manager.delete_category(category)
        print(f"Category '{category}' deleted: {deleted}")
        time.sleep(2)

    categories = manager.list_categories()
    print("Categories after deletion:", categories)
    time.sleep(2)

file_path = "questions_1_copy.json"
if not os.path.exists(file_path):
    print(f"File not found. Creating new file: {file_path}")
else:
    print(f"File found at {file_path}")

create_category_demo()
update_category_demo()
delete_category_demo()
