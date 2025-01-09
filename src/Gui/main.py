import customtkinter as ctk
from login import LoginApp

ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("dark-blue") 

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
    app.destroy()