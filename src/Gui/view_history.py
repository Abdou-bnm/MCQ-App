import customtkinter as ctk
import os
import csv
import json
from tkinter import messagebox, ttk
from utils import center_window


class ViewHistory(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.title(f"{username}'s Quiz History")
        self.geometry("900x600")
        self.resizable(False, False)
        center_window(self,900,600)
        self.username = username

        self.RESULT_DIR = f"data/results/{self.username}"
        self.USER_DATA_FILE = "data/users.json"
        os.makedirs(self.RESULT_DIR, exist_ok=True)

        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0, fg_color="#2C3E50")
        self.sidebar.pack(side="left", fill="y")

        self.sidebar_title = ctk.CTkLabel(self.sidebar, text="QCMs History", font=("Arial", 18, "bold"), text_color="#E94560")
        self.sidebar_title.pack(pady=20)

        self.summary_button = ctk.CTkButton(self.sidebar,text="📊 View Summary",command=self.display_summary,fg_color="#E94560",text_color="white",hover_color="#D32F2F")
        self.summary_button.pack(pady=10, padx=10)

        self.file_listbox = ctk.CTkScrollableFrame(self.sidebar, width=135, height=350, fg_color="#CCCCCC")
        self.file_listbox.pack(pady=20, padx=20, fill="y", expand=False)

        self.close_button = ctk.CTkButton(self.sidebar,text="Return to Main Menu",command=self.return_to_main_menu,fg_color="#E94560",text_color="white",hover_color="#D32F2F",height=40)
        self.close_button.pack(pady=20, padx=10, side="bottom")

        self.content_frame = ctk.CTkFrame(self, fg_color="#2C3E50")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.header_label = ctk.CTkLabel(self.content_frame, text="Select a Quiz File to View Details", font=("Arial", 20), text_color="white")
        self.header_label.pack(pady=20)

        self.table_frame = ctk.CTkFrame(self.content_frame, fg_color="#2C3E50")
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.display_files()        

    def display_files(self):
        """Display all result files in the user's directory."""
        try:
            files = [f for f in os.listdir(self.RESULT_DIR) if f.endswith('.csv')]
            if not files:
                label = ctk.CTkLabel(self.file_listbox, text="No quiz files found.", font=("Arial", 14), text_color="#E94560")
                label.pack(pady=5)
            else:
                for file in files:
                    btn = ctk.CTkButton(self.file_listbox,text=f"📄 {file}",command=lambda f=file: self.display_file_details(f),fg_color="#E94560",text_color="white",hover_color="#D32F2F",corner_radius=5,height=40)
                    btn.pack(pady=5, fill="x")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load files: {str(e)}")

    def display_file_details(self, filename):
        """Load and display details of the selected file."""
        try:
            file_path = os.path.join(self.RESULT_DIR, filename)
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                rows = list(reader)

            metadata = rows[1]
            category = metadata[1]
            date = metadata[2]
            score = metadata[3]
            total = metadata[4]
            percentage = metadata[5]

            self.header_label.configure(text=f"Category: {category} | Score: {score}/{total} ({percentage}%) | Date: {date}")
            self.display_table(rows)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to load details: {str(e)}")

    def display_table(self, rows):
        """Display results in a table format with colors."""
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        table = ttk.Treeview(self.table_frame, columns=("Question", "Result", "Your Answer", "Correct Answer"), show="headings")
        table.heading("Question", text="Question")
        table.heading("Result", text="Result")
        table.heading("Your Answer", text="Your Answer")
        table.heading("Correct Answer", text="Correct Answer")

        table.column("Question", width=300, anchor="w")
        table.column("Result", width=100, anchor="center")
        table.column("Your Answer", width=150, anchor="center")
        table.column("Correct Answer", width=150, anchor="center")

        vsb = ttk.Scrollbar(self.table_frame, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")
        table.pack(expand=True, fill="both")

        start_feedback = False
        for row in rows:
            if not row:
                continue
            if "Detailed Feedback" in row[0]:
                start_feedback = True
                continue

            if start_feedback:
                question = row[0]
                result = row[1]
                user_answer = row[2].replace("Your answer: ", "")
                correct_answer = row[3].replace("Correct answer: ", "")

                color = "green" if result == "Correct" else "red"
                table.insert("", "end", values=(question, result, user_answer, correct_answer), tags=(color,))

        table.tag_configure("green", background="lightgreen")
        table.tag_configure("red", background="lightcoral")

    def display_summary(self):
        """Display user's quiz history summary."""
        try:
            with open(self.USER_DATA_FILE, 'r') as file:
                users = json.load(file)

            user_history = users.get(self.username, {}).get('history', [])
            summary = "\n".join([f"{h['date']} - {h['category']} - {h['score']}" for h in user_history])

            messagebox.showinfo("Quiz Summary", summary if summary else "No history found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load summary: {str(e)}")


    def return_to_main_menu(self):
        self.destroy()
        from home_page import HomePage
        app = HomePage(username=self.username)
        app.mainloop()
    
if __name__ == "__main__":
    app = ViewHistory(username="abdou")
    app.mainloop()
