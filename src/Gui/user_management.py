import json
import os
from tkinter import messagebox
from utils import save_users, load_users
from Admin_Panel import AdminPanel
from home_page import HomePage


class UserManager:
    FILE_PATH = "data/users.json"

    def __init__(self):
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as file:
                json.dump({}, file)

    def login(self, username, password, parent_window):
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        users = load_users()
        if username in users:
            if users[username]['password'] == password:
                role = users[username]['role']     
                parent_window.withdraw() 

                if role == 'admin':
                    self.setup_admin_dashboard()
                else:
                    self.setup_student_dashboard(username)
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            users[username] = {'password': password, 'role': 'student', 'history': []}
            save_users(users)
            messagebox.showinfo("Success", "User created successfully! Login again.")
            folder_path = os.path.join("data", "results", username)
            os.makedirs(folder_path, exist_ok=True)


    def setup_admin_dashboard(self):
        app = AdminPanel()
        app.mainloop()

    def setup_student_dashboard(self, username):
        app = HomePage(username)
        app.mainloop()
