import json
from datetime import datetime


USERS_FILE = "users.json"
QUESTIONS_FILE = "questions.json"

def load_data(filepath):
    """Loads data from a JSON file."""
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(filepath, data):
    """Saves data to a JSON file."""
    with open(filepath, "w") as file:
        json.dump(data, file, indent=4)

def register_user():
    """Allows a new user to register."""
    users = load_data(USERS_FILE)
    username = input("Enter a new username: ")

    if username in users:
        print("This username already exists. Please try another one.")
        return

    password = input("Enter a password: ")
    users[username] = {"password": password, "history": []}
    save_data(USERS_FILE, users)
    print("Registration successful!")

def login_user():
    """Allows an existing user to log in."""
    users = load_data(USERS_FILE)
    username = input("Enter your username: ")

    if username not in users:
        print("Username not found.")
        return None

    password = input("Enter your password: ")
    if users[username]["password"] == password:
        print("Login successful!")
        return username

    print("Incorrect password.")
    return None

def display_user_history(username):
    """Displays a user's score history."""
    users = load_data(USERS_FILE)
    history = users.get(username, {}).get("history", [])

    if not history:
        print("You do not have any score history yet.")
    else:
        print("Your score history:")
        for entry in history:
            print(f"Date: {entry['date']}, Score: {entry['score']}")

def update_user_history(username, score=0):
    """Adds an entry to a user's history."""
    users = load_data(USERS_FILE)

    if username not in users:
        print("User not found.")
        return

    new_entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "score": score
    }
    users[username]["history"].append(new_entry)
    save_data(USERS_FILE, users)
    print("History updated.")

def main():
    """Main entry point for the user management system."""
    while True:
        print("\nUser Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            username = login_user()
            if username:
                display_user_history(username)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
