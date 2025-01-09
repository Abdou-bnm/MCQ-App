import customtkinter as ctk
from qcm_app import QCMApp
from view_history import ViewHistory
from utils import center_window
        
class HomePage(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        
        self.username = username 
        
        self.title(f"Home - {username}")
        self.geometry("500x390")
        self.configure(fg_color="#2C3E50")
        self.resizable(False, False)
        center_window(self,500,390)
        
        self.label_title = ctk.CTkLabel(self, text=f"Welcome, {username}!", font=("Arial", 24, "bold"), text_color="#E94560")
        self.label_title.pack(pady=20)

        self.label_subtitle = ctk.CTkLabel(self, text="Choose an option below:", font=("Arial", 16), text_color="#ECF0F1")
        self.label_subtitle.pack(pady=10)

        self.btn_start_quiz = ctk.CTkButton(self, text="Start Quiz", command=self.start_quiz, font=("Arial", 18), height=50, width=250,corner_radius=10,fg_color="#E94560", hover_color="#B23A48")
        self.btn_start_quiz.pack(pady=15)

        self.btn_view_history = ctk.CTkButton(self, text="View History", command=self.view_history,font=("Arial", 18), height=50, width=250,corner_radius=10,fg_color="#E94560", hover_color="#B23A48")
        self.btn_view_history.pack(pady=15)

        self.btn_logout = ctk.CTkButton(self, text="Logout", command=self.logout, font=("Arial", 18), height=50, width=250,corner_radius=10,fg_color="#E94560", hover_color="#B23A48")
        self.btn_logout.pack(pady=15)

    def start_quiz(self):
        self.destroy()
        app = QCMApp(username=self.username) 
        app.mainloop()
        self = HomePage(self.username) 
        self.mainloop()

    def view_history(self):
        self.destroy()
        app = ViewHistory(self.username)
        app.mainloop()
        self = HomePage(self.username) 
        self.mainloop()
        

    def logout(self):
        self.destroy()
        from login import LoginApp
        app = LoginApp() 
        app.mainloop()

if __name__ == "__main__":
    app = HomePage(username="abdou")
    app.mainloop()
