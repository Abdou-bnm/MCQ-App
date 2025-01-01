import customtkinter as ctk
from tkinter import messagebox
from dashboard import DashboardApp
from utils import load_users, save_users
ctk.set_appearance_mode("light") 
ctk.set_default_color_theme("dark-blue") 

# Main execution
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login System")
        self.geometry("400x300")
        
        self.label_title = ctk.CTkLabel(self, text="Login System", font=("Arial", 20))
        self.label_title.pack(pady=20)

        self.label_username = ctk.CTkLabel(self, text="Username:")
        self.label_username.pack(pady=5)
        self.entry_username = ctk.CTkEntry(self, width=200)
        self.entry_username.pack(pady=5)

        self.label_password = ctk.CTkLabel(self, text="Password:")
        self.label_password.pack(pady=5)
        self.entry_password = ctk.CTkEntry(self, width=200, show="*")
        self.entry_password.pack(pady=5)

        self.button_login = ctk.CTkButton(self, text="Login", command=self.login)
        self.button_login.pack(pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if not username or not password:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        users = load_users()
        if username in users:
            if users[username]['password'] == password:
                role = users[username]['role']
                self.withdraw()  # Hide instead of destroying
                dashboard = DashboardApp(username, role)
                dashboard.deiconify()  # Restore dashboard
                dashboard.lift()      # Bring dashboard to the top
            else:
                messagebox.showerror("Error", "Invalid password")
        else:
            users[username] = {'password': password, 'role': 'student', 'history': []}
            save_users(users)
            messagebox.showinfo("Success", "User created successfully! Login again.")

