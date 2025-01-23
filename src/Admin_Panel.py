import customtkinter as ctk
from tkinter import messagebox, simpledialog, ttk
from utils import load_questions, save_questions
import json

ctk.set_appearance_mode("light")  
ctk.set_default_color_theme("blue")  

class AdminPanel(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Manage Questions")
        self.geometry("800x600")
        self.questions = load_questions()
        self.users = self.load_users()
        
        self.configure(fg_color=("white", "#2C3E50"))

        self.sidebar = ctk.CTkFrame(
            self, width=150, fg_color=("#E8F5FA", "#1F6AA5"), corner_radius=0
        )
        self.sidebar.pack(side="left", fill="y")

        self.label_title = ctk.CTkLabel(
            self.sidebar, text="Quizzy", font=("Arial", 18, "bold"), text_color=("#1F6AA5", "#E8F5FA")
        )
        self.label_title.pack(pady=10)

        self.btn_questions = ctk.CTkButton(
            self.sidebar, text="Questions", 
            command=self.show_questions_tab , 
            fg_color=("white", "#1F6AA5"),          
            border_color=("#1F6AA5", "#E8F5FA"),    
            border_width=2,                        
            text_color=("#1F6AA5", "#E8F5FA"),
            hover_color=("#D6E4FF", "#4A90E2")   
        )
        self.btn_questions.pack(padx=20, pady=10)

        self.btn_categories = ctk.CTkButton(
            self.sidebar, text="Categories", 
            command=self.show_categories_tab ,
            fg_color=("white", "#1F6AA5"),        
            border_color=("#1F6AA5", "#E8F5FA"), 
            border_width=2,                     
            text_color=("#1F6AA5", "#E8F5FA"),  
            hover_color=("#D6E4FF", "#4A90E2")      
        )
        self.btn_categories.pack(padx=20, pady=10)

        self.btn_users = ctk.CTkButton(
            self.sidebar, text="Users", 
            command=self.show_users_tab,
            fg_color=("white", "#1F6AA5"),      
            border_color=("#1F6AA5", "#E8F5FA"),     
            border_width=2,                       
            text_color=("#1F6AA5", "#E8F5FA"),  
            hover_color=("#D6E4FF", "#4A90E2")    
        )
        self.btn_users.pack(padx=20, pady=10)

        ctk.CTkFrame(self.sidebar, fg_color="transparent").pack(expand=True, fill="y")

        def toggle_mode():
            if switch_var.get():  
                ctk.set_appearance_mode("dark") 
            else:
                ctk.set_appearance_mode("light") 

        switch_var = ctk.BooleanVar(value=False)
        self.btn_mode = ctk.CTkSwitch(
            self.sidebar,
            text="Switch Mode",
            command=toggle_mode,
            variable=switch_var,
            fg_color=("lightgray", "#1F6AA5"),
            progress_color=("blue", "white")
        )
        self.btn_mode.pack(pady=10)

        self.btn_home = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            command=self.Logout,
            fg_color=("white", "#1F6AA5"),           
            border_color=("#1F6AA5", "#E8F5FA"),   
            border_width=2,                         
            text_color=("#1F6AA5", "#E8F5FA"),       
            hover_color=("#D6E4FF", "#4A90E2")     
        )
        self.btn_home.pack(pady=10, padx=20)

        self.tabs = ctk.CTkFrame(self, fg_color=("white", "#34495E"))
        self.tabs.pack(side="right", fill="both", expand=True)

        self.show_questions_tab()


    ###############################################################################################
    
    def show_questions_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        self.label_title = ctk.CTkLabel(self.tabs, text="Manage Questions", font=("Arial", 18, "bold"))
        self.label_title.pack(pady=10)

        table_frame = ctk.CTkFrame(self.tabs, fg_color="transparent") 
        table_frame.pack(padx=10, pady=10, fill="both", expand=True)

        tree_scroll_y = ttk.Scrollbar(table_frame, orient="vertical")
        tree_scroll_y.pack(side="right", fill="y")

        tree_scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        tree_scroll_x.pack(side="bottom", fill="x")

        self.tree = ttk.Treeview(
            table_frame, 
            columns=("Question", "Category", "Correct"), 
            show="headings",
            yscrollcommand=tree_scroll_y.set, 
            xscrollcommand=tree_scroll_x.set
        )

        tree_scroll_y.config(command=self.tree.yview)
        tree_scroll_x.config(command=self.tree.xview)

        self.tree.heading("Question", text="Question Text", anchor="w")
        self.tree.heading("Category", text="Category", anchor="center")
        self.tree.heading("Correct", text="Correct Answer", anchor="center")

        self.tree.column("Question", anchor="w", width=460)
        self.tree.column("Category", anchor="center", width=120)
        self.tree.column("Correct", anchor="center", width=120)

        self.tree.pack(fill="both", expand=True)

        for category, questions in self.questions.items():
            for question in questions:
                self.tree.insert("", "end", values=(question["question"], category, question["correct"]))

        frame = ctk.CTkFrame(self.tabs, fg_color="transparent")  # Transparent frame
        frame.pack(pady=20, padx=20)

        self.btn_add = ctk.CTkButton(
            frame,
            text="Add Question",
            text_color="#ffffff",
            command=self.add_question, 
        )
        self.btn_add.grid(row=0, column=0, padx=10)

        self.btn_edit = ctk.CTkButton(
            frame,
            text="Edit Question",
            text_color="#ffffff",
            command=self.edit_question, 
        )
        self.btn_edit.grid(row=0, column=1, padx=10)

        self.btn_delete = ctk.CTkButton(
            frame,
            text="Delete Question",
            command=self.delete_question,
            fg_color="#E53935", 
            text_color="#ffffff",
            hover_color="#D32F2F"  
        )
        self.btn_delete.grid(row=0, column=2, padx=10)

    def add_question(self):
        category = simpledialog.askstring("Input", "Enter Category:")
        if not category:
            messagebox.showerror("Error", "Category cannot be empty.")
            return

        if category not in self.questions:
            messagebox.showerror("Error", "Category does not exist.")
            return

        question_text = simpledialog.askstring("Input", "Enter Question Text:")
        if not question_text:
            messagebox.showerror("Error", "Question text cannot be empty.")
            return

        options = simpledialog.askstring("Input", "Enter Options (comma-separated):")
        if not options:
            messagebox.showerror("Error", "Options cannot be empty.")
            return

        correct = simpledialog.askstring("Input", "Enter Correct Option (a, b, c...):")
        if not correct or correct.lower() not in [chr(i) for i in range(97, 97 + len(options.split(',')))]:
            messagebox.showerror("Error", "Invalid correct option.")
            return

        new_question = {"question": question_text, "options": options.split(','), "correct": correct}
        self.questions[category].append(new_question)
        save_questions(self.questions)
        messagebox.showinfo("Success", "Question added successfully!")
        self.show_questions_tab()

    def edit_question(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No question selected.")
            return

        values = self.tree.item(selected, "values")
        category = values[1]
        old_question_text = values[0]

        question_text = simpledialog.askstring("Edit", "Edit Question Text:", initialvalue=old_question_text)
        options = simpledialog.askstring("Edit", "Edit Options (comma-separated):")
        correct = simpledialog.askstring("Edit", "Edit Correct Option:")

        for question in self.questions[category]:
            if question['question'] == old_question_text:
                question.update({"question": question_text, "options": options.split(','), "correct": correct})
                break

        save_questions(self.questions)
        messagebox.showinfo("Success", "Question updated successfully!")
        self.show_questions_tab()

    # Delete Question
    def delete_question(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "No question selected.")
            return

        values = self.tree.item(selected, "values")
        category = values[1]
        question_text = values[0]

        confirm = messagebox.askyesno("Confirm", f"Delete question: '{question_text}'?")
        if confirm:
            self.questions[category] = [q for q in self.questions[category] if q['question'] != question_text]
            save_questions(self.questions)
            messagebox.showinfo("Success", "Question deleted successfully!")
            self.show_questions_tab()

    ###############################################################################################
    
    def show_categories_tab(self):
        for widget in self.tabs.winfo_children():
            widget.destroy()

        self.label_title = ctk.CTkLabel(self.tabs, text="Manage Categories", font=("Arial", 18))
        self.label_title.pack(pady=10)

        frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        category_scroll_y = ttk.Scrollbar(frame, orient="vertical")
        category_scroll_y.pack(side="right", fill="y")

        self.category_listbox = ttk.Treeview(
            frame,
            columns=("Category",),
            show="headings",
            yscrollcommand=category_scroll_y.set
        )

        category_scroll_y.config(command=self.category_listbox.yview)

        self.category_listbox.heading("Category", text="Categories", anchor="w")
        self.category_listbox.column("Category", anchor="w", width=300)

        for category in self.questions.keys():
            self.category_listbox.insert("", "end", values=(category,))

        self.category_listbox.pack(fill="both", expand=True, padx=10, pady=10)

        button_frame = ctk.CTkFrame(self.tabs, fg_color="transparent")
        button_frame.pack(pady=10)

        self.btn_add_category = ctk.CTkButton(button_frame, text="Add Category",text_color="#ffffff" ,command=self.add_category)
        self.btn_add_category.grid(row=0, column=0, padx=10)

        self.btn_delete_category = ctk.CTkButton(button_frame, text="Delete Category",fg_color="#E53935",text_color="#ffffff",hover_color="#D32F2F",command=self.delete_category)
        self.btn_delete_category.grid(row=0, column=1, padx=10)


    def render_categories(self):
        for item in self.category_listbox.get_children():
            self.category_listbox.delete(item)

        for category in self.questions.keys():
            self.category_listbox.insert("", "end", values=(category,))
        
    def add_category(self):
        category = simpledialog.askstring("Input", "Enter Category Name:")
        if category in self.questions:
            messagebox.showerror("Error", "Category already exists.")
            return
        self.questions[category] = []
        save_questions(self.questions)
        messagebox.showinfo("Success", "Category added successfully!")
        self.render_categories()

    def delete_category(self):
        category = simpledialog.askstring("Input", "Enter Category Name to Delete:")
        if category not in self.questions:
            messagebox.showerror("Error", "Category does not exist.")
            return
        confirm = messagebox.askyesno("Confirm", f"Delete category: '{category}'? This will delete all related questions.")
        if confirm:
            del self.questions[category]
            save_questions(self.questions)
            messagebox.showinfo("Success", "Category deleted successfully!")
            self.render_categories()

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

        btn_add_user = ctk.CTkButton(
            frame,
            text="Add User",
            text_color="#ffffff",
            command=self.add_user
        )
        btn_add_user.grid(row=0, column=0, padx=10)

        btn_edit_user = ctk.CTkButton(
            frame, 
            text="Edit User", 
            text_color="#ffffff",
            command=self.edit_user
        )
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
        role = simpledialog.askstring("Add User", "Enter Role (admin/student):")
        self.users[username] = {"role": role}
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