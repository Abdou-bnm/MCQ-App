import customtkinter as ctk
from utils import load_users, center_window
from evaluation_system import EvaluationSystem
from difficulty_based_timer import DifficultyTimer
import json


class QCMApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()

        self.evaluator = EvaluationSystem()

        self.username = username
        self.users = load_users()
        self.questions = self.load_questions()
        self.selected_category = None
        self.selected_level = None
        self.question_list = []
        self.timer = None
        self.difficulty_timer = None

        self.title("QCM Test")
        self.geometry("800x600")
        center_window(self, 800, 600)
        self.resizable(False, False)
        self.configure(fg_color="#2C3E50")

        self.sidebar = ctk.CTkFrame(self, width=150, fg_color=("#E94560", "#34495E"), corner_radius=0)
        self.sidebar.pack(side="left", fill="y", padx=5)
        self.label_title = ctk.CTkLabel(self.sidebar, text="Quizzy", font=("Arial", 18, "bold"), text_color=("#FFFFFF", "#E94560"))
        self.label_title.pack(pady=(20, 10))
        ctk.CTkFrame(self.sidebar, fg_color="transparent").pack(expand=True, fill="y")
        self.btn_home = ctk.CTkButton(self.sidebar,text="Main Menu",command=self.return_to_main_menu,fg_color=("white", "#E94560"),border_color=("#E94560", "#E94560"),border_width=2,text_color=("#E94560", "white"),hover_color=("#F76C81", "#F76C81"),)
        self.btn_home.pack(pady=10, padx=20)

        self.main_content = ctk.CTkFrame(self, fg_color="#2C3E50")
        self.main_content.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.show_categories()

    def load_questions(self):
        with open("data/questions_1.json", "r") as file:
            data = json.load(file)
        return data["categories"]

    def show_categories(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.main_content, text="Select Category", font=("Arial", 24), text_color="#E94560"
        ).pack(pady=20)

        scroll_frame = ctk.CTkScrollableFrame(self.main_content, width=600, height=400, fg_color="#34495E")
        scroll_frame.pack(pady=20, padx=20, fill="both", expand=True)

        for category in self.questions:
            btn = ctk.CTkButton(scroll_frame,text=category["name"],command=lambda c=category: self.show_levels(c),font=("Arial", 18),width=300,height=50,fg_color="#E94560",text_color="white",hover_color="#B23A48",)
            btn.pack(pady=10)

    def show_levels(self, category):
        self.selected_category = category
        for widget in self.main_content.winfo_children():
            widget.destroy()

        ctk.CTkLabel(self.main_content, text=f"Category: {category['name']}", font=("Arial", 24), text_color="#E94560").pack(pady=20)
        ctk.CTkLabel(self.main_content, text="Select Level", font=("Arial", 20), text_color="white").pack(pady=10)

        for level in category["levels"]:
            btn = ctk.CTkButton(self.main_content,text=level["level"].capitalize(),command=lambda l=level: self.start_qcm(l),font=("Arial", 18),width=300,height=50,fg_color="#E94560",text_color="white",hover_color="#B23A48",)
            btn.pack(pady=10)

    def start_qcm(self, level):
        self.selected_level = level
        self.question_list = level["questions"]
        self.current_question_index = 0

        self.evaluator = EvaluationSystem()

        difficulty = level["level"].lower()
        self.difficulty_timer = DifficultyTimer(difficulty)

        self.show_question()

    def show_question(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        if self.current_question_index >= len(self.question_list):
            self.show_result()
            return

        question_data = self.question_list[self.current_question_index]
        ctk.CTkLabel(self.main_content, text=question_data["question"], font=("Arial", 20), text_color="white").pack(pady=20)

        self.buttons = []
        for i, option in enumerate(question_data["options"]):
            btn = ctk.CTkButton(self.main_content,text=option,command=lambda i=i: self.check_answer(i),font=("Arial", 16),width=500,height=40,fg_color="#E94560",text_color="white",hover_color="#B23A48",)
            btn.pack(pady=5)
            self.buttons.append(btn)

        self.difficulty_timer.reset()
        self.timer_label = ctk.CTkLabel(self.main_content, text=self.difficulty_timer.get_formatted_time(), font=("Arial", 18), text_color="white")
        self.timer_label.pack(pady=10)
        self.update_timer()

    def update_timer(self):
        self.difficulty_timer.update()
        self.timer_label.configure(text=self.difficulty_timer.get_formatted_time())

        if self.difficulty_timer.time_left > 0:
            self.timer = self.after(1000, self.update_timer)
        else:
            self.check_answer(None)

    def check_answer(self, selected_index):
        self.after_cancel(self.timer)
        question_data = self.question_list[self.current_question_index]
        correct_index = question_data["correct"]

        for btn in self.buttons:
            btn.configure(state="disabled")

        user_answer = question_data["options"][selected_index] if selected_index is not None else ""
        correct_answer = question_data["options"][correct_index]
        is_correct = self.evaluator.evaluate_answer(question_data["question"], user_answer, correct_answer)

        if selected_index is not None:
            if is_correct:
                self.buttons[selected_index].configure(fg_color="green", text_color="white")
            else:
                self.buttons[selected_index].configure(fg_color="red", text_color="white")
                self.buttons[correct_index].configure(fg_color="green", text_color="white")
        else:
            self.buttons[correct_index].configure(fg_color="green", text_color="white")

        self.after(3000, self.next_question)

    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def show_result(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

        score_data = self.evaluator.calculate_final_score(len(self.question_list))
        feedback_summary = self.evaluator.generate_feedback_summary()

        ctk.CTkLabel(self.main_content, text="Test Completed!", font=("Arial", 24), text_color="#E94560").pack(pady=20)
        ctk.CTkLabel(self.main_content,text=f"Your Score: {score_data['raw_score']}/{score_data['total_questions']} ({score_data['percentage']}%)",font=("Arial", 20),text_color="white",).pack(pady=10)

        self.evaluator.update_user_history(self.username, score_data, self.selected_category["name"])
        self.evaluator.export_results(self.username, self.selected_category, score_data)
                
        ctk.CTkLabel(self.main_content, text="Feedback:", font=("Arial", 18), text_color="white").pack(pady=10)
        ctk.CTkLabel(self.main_content, text=feedback_summary, font=("Arial", 14), wraplength=700, text_color="white").pack(pady=10)

        ctk.CTkButton(self.main_content,text="Back to Main Menu",command=self.return_to_main_menu,font=("Arial", 18),width=300,height=50,fg_color="#E94560",text_color="white",hover_color="#B23A48",).pack(pady=20)


    def return_to_main_menu(self):
        self.destroy()
        from home_page import HomePage
        app = HomePage(username=self.username)
        app.mainloop()


if __name__ == "__main__":
    app = QCMApp("abdou")
    app.mainloop()
