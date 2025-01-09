import customtkinter as ctk
from user_management import UserManager
from utils import center_window


class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.user_manager = UserManager()
        self.title("Login System")
        self.geometry("400x350")
        center_window(self,400,350)
        self.resizable(False, False)
        
        self.login_frame = ctk.CTkFrame(self, fg_color="#2C3E50")
        self.login_frame.pack(expand=True, fill="both")

        self.avatar_label = ctk.CTkLabel(self.login_frame, text="👤", font=("Arial", 60), text_color="#E94560")
        self.avatar_label.pack(pady=10)

        self.sign_in_label = ctk.CTkLabel(self.login_frame, text="Sign In", font=("Arial", 28, "bold"), text_color="#E94560")
        self.sign_in_label.pack(pady=10)

        self.entry_username = ctk.CTkEntry(self.login_frame, width=300, height=45, placeholder_text="Enter your username",fg_color="#2C3E50", text_color="white", border_color="#E94560", placeholder_text_color="#B0BEC5")
        self.entry_username.pack(pady=5)

        self.entry_password = ctk.CTkEntry(self.login_frame, width=300, height=45, placeholder_text="Enter your password", show="*",fg_color="#2C3E50", text_color="white", border_color="#E94560", placeholder_text_color="#B0BEC5")
        self.entry_password.pack(pady=5)

        self.button_login = ctk.CTkButton(self.login_frame, text="LOGIN", width=300, height=45,command=lambda: self.user_manager.login(self.entry_username.get(), self.entry_password.get(), self), fg_color="#E94560",text_color="white",hover_color="#D32F2F")
        self.button_login.pack(pady=25)


if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
