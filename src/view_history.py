import customtkinter as ctk
import json

class ViewHistory(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.title("User History")
        self.geometry("600x400")
        self.username = username

        # Load user data
        self.users = self.load_users()
        self.history = self.users.get(self.username, [])

        # UI Components
        self.title_label = ctk.CTkLabel(self, text=f"{self.username}'s History", font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Scrollable Frame
        self.scroll_frame = ctk.CTkScrollableFrame(self, width=500, height=300)
        self.scroll_frame.pack(pady=10, padx=20)

        # Load History Data
        self.display_history()

        # Close Button
        self.close_button = ctk.CTkButton(self, text="Close", command=self.destroy)
        self.close_button.pack(pady=10)

    def load_users(self):
        try:
            with open('data/users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def display_history(self):
        # Extract history from user data
        user_data = self.users.get(self.username, {})
        self.history = user_data.get('history', [])  # Get only history field

        # Display history entries
        if not self.history:
            label = ctk.CTkLabel(self.scroll_frame, text="No history available.", font=("Arial", 16))
            label.pack(pady=5)
        else:
            for entry in self.history:
                # Validate each entry
                if isinstance(entry, dict) and 'date' in entry and 'score' in entry and 'category' in entry:
                    date = entry['date']
                    score = entry['score']
                    category = entry['category']
                    text = f"Date: {date} | Category: {category} | Score: {score}"
                else:
                    text = f"Invalid data: {entry}"

                label = ctk.CTkLabel(self.scroll_frame, text=text, font=("Arial", 14))
                label.pack(pady=5)

