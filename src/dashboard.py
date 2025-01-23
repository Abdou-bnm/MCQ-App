import customtkinter as ctk
from qcm_app import QCMApp
from view_history import ViewHistory
from Admin_Panel import AdminPanel

class DashboardApp(ctk.CTk):
    def __init__(self, username, role):
        super().__init__()
        self.username = username
        self.role = role
        self.title(f"Dashboard - {self.username}")
        self.geometry("600x400")

        self.label_title = ctk.CTkLabel(self, text=f"Welcome, {self.username}!", font=("Arial", 20))
        self.label_title.pack(pady=20)

        if self.role == 'admin':
            self.setup_admin_dashboard()
        else:
            self.setup_student_dashboard()

    def setup_admin_dashboard(self):
        self.destroy()
        app = AdminPanel()
        app.mainloop()

    def setup_student_dashboard(self):
        
        self.btn_start_test = ctk.CTkButton(self, text="Start Test", command=self.start_test)
        self.btn_start_test.pack(pady=10)

        self.btn_view_history = ctk.CTkButton(self, text="View History", command=self.view_history)
        self.btn_view_history.pack(pady=10)

        self.btn_logout = ctk.CTkButton(self,fg_color=("black", "lightgray"), text="Logout", command=self.logout)
        self.btn_logout.pack(pady=10)


    def start_test(self):
        self = QCMApp(username=self.username)
        self.mainloop()

    def view_history(self):
        self = ViewHistory(username=self.username)
        self.mainloop()

    def logout(self):
        self.destroy()
        from login import LoginApp
        app = LoginApp() 
        app.mainloop()

        
if __name__ == "__main__":
    app = DashboardApp("abdou","admin")
    app.mainloop()