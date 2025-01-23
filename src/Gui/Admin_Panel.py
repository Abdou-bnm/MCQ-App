import customtkinter as ctk
from tkinter import messagebox, simpledialog, ttk
from utils import load_questions
from utils import center_window
from QuestionManager import QuestionManager
from category import CategoryManager
import json
import os

ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()

        
        
        self.title("Admin Panel")
        self.geometry("800x600")
        self.resizable(False, False)
        center_window(self,800,600)
        self.questions = load_questions()
        self.users = self.load_users()
        
        self.file_path = "data/questions_1.json"
        self.user_path = "data/users.json"
        self.user_file_path = "data/users.json"
        self.question_manager = QuestionManager(self.file_path)
        self.category_manager = CategoryManager(self.file_path)
        self.users = self.load_users()

        # Apply Theme Colors
        self.configure(fg_color=("white", "#2C3E50"))

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=150, fg_color=("#E94560", "#2C3E50"), corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        self.label_title = ctk.CTkLabel(self.sidebar, text="Quizzy", font=("Arial", 18, "bold"), text_color=("#FFFFFF", "#E94560"))
        self.label_title.pack(pady=10)

        self.btn_questions = ctk.CTkButton(self.sidebar,text="Questions",command=self.show_questions_tab,fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),)
        self.btn_questions.pack(padx=20, pady=10)

        self.btn_categories = ctk.CTkButton(self.sidebar,text="Categories",command=self.show_categories_tab,fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),)
        self.btn_categories.pack(padx=20, pady=10)

        self.btn_users = ctk.CTkButton(self.sidebar,text="Users",command=self.show_users_tab,fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),)
        self.btn_users.pack(padx=20, pady=10)

        ctk.CTkFrame(self.sidebar, fg_color="transparent").pack(expand=True, fill="y")

        # Light/Dark Mode Toggle
        def toggle_mode():
            if switch_var.get():
                ctk.set_appearance_mode("dark")
            else:
                ctk.set_appearance_mode("light")

        switch_var = ctk.BooleanVar(value=False)
        self.btn_mode = ctk.CTkSwitch(self.sidebar,text="Switch Mode",command=toggle_mode,variable=switch_var,fg_color=("lightgray", "#E94560"),progress_color=("#E94560", "white"),)
        self.btn_mode.pack(pady=10)

        self.btn_home = ctk.CTkButton(self.sidebar,text="Logout",command=self.Logout,fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),)
        self.btn_home.pack(pady=10, padx=20)

        self.tabs = ctk.CTkFrame(self, fg_color=("white", "#34495E"))
        self.tabs.pack(side="right", fill="both", expand=True)

        self.show_questions_tab()

    def show_questions_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.tabs, text="Manage Questions", font=("Arial", 18, "bold")).pack(pady=10)

        table_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tree_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scroll_y.pack(side="right", fill="y")

        self.tree = ttk.Treeview(table_frame,columns=("ID", "Question", "Category", "Level", "Correct"),show="headings",yscrollcommand=tree_scroll_y.set,)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Question", text="Question")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Level", text="Level")
        self.tree.heading("Correct", text="Correct Option")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Question", width=300, anchor="w")
        self.tree.column("Category", width=100, anchor="center")
        self.tree.column("Level", width=100, anchor="center")
        self.tree.column("Correct", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)
        tree_scroll_y.config(command=self.tree.yview)

        self.refresh_questions()

        button_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        button_frame.pack(pady=10)

        add_button = ctk.CTkButton(
            self.sidebar, 
            text="Add Question", 
            command=self.add_question, 
            fg_color="#E94560", 
            text_color="white", 
            hover_color="#D32F2F"
        )
        add_button.pack(pady=10, padx=20)

        ctk.CTkButton(button_frame, text="Edit Question", command=self.edit_question).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Delete Question", command=self.delete_question).pack(side="left", padx=10)

    def show_questions_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.tabs, text="Manage Questions", font=("Arial", 18, "bold")).pack(pady=10)

        table_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tree_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scroll_y.pack(side="right", fill="y")

        self.tree = ttk.Treeview(table_frame,columns=("ID", "Question", "Category", "Level", "Correct"),show="headings",yscrollcommand=tree_scroll_y.set,)

        self.tree.heading("ID", text="ID")
        self.tree.heading("Question", text="Question")
        self.tree.heading("Category", text="Category")
        self.tree.heading("Level", text="Level")
        self.tree.heading("Correct", text="Correct Option")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Question", width=300, anchor="w")
        self.tree.column("Category", width=100, anchor="center")
        self.tree.column("Level", width=100, anchor="center")
        self.tree.column("Correct", width=100, anchor="center")

        self.tree.pack(fill="both", expand=True)
        tree_scroll_y.config(command=self.tree.yview)

        self.refresh_questions()

        button_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Add Question", command=self.add_question).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Edit Question", command=self.edit_question).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Delete Question", command=self.delete_question).pack(side="left", padx=10)

    def refresh_questions(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        categories = self.category_manager._load_data()["categories"]
        for category in categories:
            for level in category["levels"]:
                for question in level["questions"]:
                    self.tree.insert(
                        "",
                        "end",
                        values=(question["id"], question["question"], category["name"], level["level"], question["correct"]),
                    )

    def add_question(self):
        """Add a new question using QuestionManager."""
        try:
            # Gather inputs from the user
            category = simpledialog.askstring("Category", "Enter category name:")
            if not category:
                messagebox.showerror("Error", "Category name cannot be empty.")
                return

            level = simpledialog.askstring("Level", "Enter level (easy, medium, hard):")
            if level not in ["easy", "medium", "hard"]:
                messagebox.showerror("Error", "Invalid level. Please enter 'easy', 'medium', or 'hard'.")
                return

            question_text = simpledialog.askstring("Question", "Enter question text:")
            if not question_text:
                messagebox.showerror("Error", "Question text cannot be empty.")
                return

            options = simpledialog.askstring("Options", "Enter options (comma-separated):")
            if not options:
                messagebox.showerror("Error", "Options cannot be empty.")
                return
            options = options.split(",")
            if len(options) < 2:
                messagebox.showerror("Error", "You must provide at least two options.")
                return

            correct = simpledialog.askstring("Correct Option", "Enter the index of the correct option (0-based):")
            if not correct or not correct.isdigit() or int(correct) < 0 or int(correct) >= len(options):
                messagebox.showerror("Error", "Invalid correct option index.")
                return
            correct = int(correct)

            # Call QuestionManager to add the question
            self.question_manager.add_question(category, level, question_text, options, correct)

            # Refresh the GUI table
            self.refresh_questions()

            # Success feedback
            messagebox.showinfo("Success", "Question added successfully!")
        except ValueError as ve:
            messagebox.showerror("Error", f"Validation Error: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")



    def edit_question(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No question selected.")
            return

        question_id = int(self.tree.item(selected)["values"][0])
        new_question_text = simpledialog.askstring("Edit Question", "Enter new question text (optional):")
        new_options = simpledialog.askstring("Edit Options", "Enter new options (comma-separated) (optional):")
        new_correct = simpledialog.askstring("Edit Correct Option", "Enter new correct option index (optional):")

        new_correct = int(new_correct) if new_correct else None
        new_options = new_options.split(",") if new_options else None

        self.question_manager.edit_question(question_id, new_question_text, new_options, new_correct)
        messagebox.showinfo("Success", "Question updated successfully!")
        self.refresh_questions()

    def delete_question(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No question selected.")
            return

        question_id = int(self.tree.item(selected)["values"][0])
        self.question_manager.delete_question(question_id)
        messagebox.showinfo("Success", "Question deleted successfully!")
        self.refresh_questions()

    def show_categories_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.tabs, text="Manage Categories", font=("Arial", 18, "bold")).pack(pady=10)

        self.category_list = ttk.Treeview(self.tabs, columns=("Category"), show="headings")
        self.category_list.heading("Category", text="Category")
        self.category_list.column("Category", anchor="center", width=200)
        self.category_list.pack(fill="both", expand=True)

        self.refresh_categories()

        button_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Add Category", command=self.add_category).pack(side="left", padx=10)
        ctk.CTkButton(button_frame, text="Delete Category", command=self.delete_category).pack(side="left", padx=10)

    def refresh_categories(self):
        for row in self.category_list.get_children():
            self.category_list.delete(row)

        categories = self.category_manager.list_categories()
        for category in categories:
            self.category_list.insert("", "end", values=(category,))

    def add_category(self):
        name = simpledialog.askstring("Add Category", "Enter category name:")
        if self.category_manager.create_category(name):
            messagebox.showinfo("Success", "Category added successfully!")
            self.refresh_categories()
        else:
            messagebox.showerror("Error", "Category already exists.")

    def delete_category(self):
        selected = self.category_list.selection()
        if not selected:
            messagebox.showerror("Error", "No category selected.")
            return

        category_name = self.category_list.item(selected)["values"][0]
        if self.category_manager.delete_category(category_name):
            messagebox.showinfo("Success", "Category deleted successfully!")
            self.refresh_categories()
        else:
            messagebox.showerror("Error", "Category not found.")

    ###############################################################################################

    def load_users(self):
        try:
            with open('data/users.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open('data/users.json', 'w') as f:
            json.dump(self.users, f, indent=4)

    def show_users_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        label_title = ctk.CTkLabel(self.tabs, text="Manage Users", font=("Arial", 18))
        label_title.pack(pady=10)

        table_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(
            table_frame,
            columns=("Username", "Role"),
            show="headings"
        )
        self.tree.heading("Username", text="Username")
        self.tree.heading("Role", text="Role")
        self.tree.pack(fill="both", expand=True)

        self.refresh_users_table()

        frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        frame.pack(pady=20, padx=20)

        btn_add_user = ctk.CTkButton(frame,text="Add User",fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),command=self.add_user)
        btn_add_user.grid(row=0, column=0, padx=10)

        btn_edit_user = ctk.CTkButton(frame, text="Edit User", fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),command=self.edit_user)
        btn_edit_user.grid(row=0, column=1, padx=10)

        btn_delete_user = ctk.CTkButton(frame, text="Delete User", command=self.delete_user,fg_color="#E53935", text_color="#ffffff",hover_color="#D32F2F")
        btn_delete_user.grid(row=0, column=2, padx=10)
        
        
    def refresh_users_table(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for username, details in self.users.items():
            self.tree.insert("", "end", values=(username, details['role']))

    def add_user(self):
        username = simpledialog.askstring("Add User", "Enter Username:")
        if username in self.users:
            messagebox.showerror("Error", "User already exists.")
            return
        password = simpledialog.askstring("Add User", "Enter Password:")
        role = simpledialog.askstring("Add User", "Enter Role (admin/student):")
        self.users[username] = {"password": password ,"role": role , "history": []}
        with open(self.user_path, 'w') as file:
            json.dump(self.users, file, indent=4)
        folder_path = os.path.join("data", "results", username)
        os.makedirs(folder_path, exist_ok=True)
        self.save_users()
        self.refresh_users_table()

    def edit_user(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No user selected.")
            return
        username = self.tree.item(selected, "values")[0]
        role = simpledialog.askstring("Edit Role", "Enter new role (admin/student):")
        self.users[username]["role"] = role
        self.save_users()
        self.refresh_users_table()

    def delete_user(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No user selected.")
            return
        username = self.tree.item(selected, "values")[0]
        confirm = messagebox.askyesno("Delete User", f"Are you sure you want to delete {username}?")
        if confirm:
            del self.users[username]
            self.save_users()
            self.refresh_users_table()

    def Logout(self):
        self.destroy()
        from login import LoginApp
        app = LoginApp() 
        app.mainloop()
        
if __name__ == "__main__":
    app = AdminPanel()
    app.mainloop()