import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime
from utils import load_users, save_users, load_questions
from Logic.evaluation_system import EvaluationSystem


class QCMApp(ctk.CTk):
    def __init__(self, username):
        super().__init__()

        # Initialize Evaluation System
        self.evaluator = EvaluationSystem()

        # User and Questions Data
        self.username = username
        self.users = load_users()
        self.questions = load_questions()
        self.selected_category = None
        self.question_list = []
        self.timer = None
        self.time_left = 15

        # Configure Window
        self.title("QCM Test")
        self.geometry("800x600")
        self.show_categories()

    # --- Show Categories ---
    def show_categories(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Title
        ctk.CTkLabel(self, text="Select Category", font=("Arial", 24)).pack(pady=20)

        # Category Buttons
        for category in self.questions.keys():
            btn = ctk.CTkButton(
                self,
                text=category,
                command=lambda c=category: self.start_qcm(c),
                font=("Arial", 18),  # Larger Font
                width=300,          # Wider Buttons
                height=50           # Taller Buttons
            )
            btn.pack(pady=10)

    # --- Start QCM ---
    def start_qcm(self, category):
        self.selected_category = category
        self.question_list = self.questions[category]
        self.current_question_index = 0

        # Reset Evaluator
        self.evaluator = EvaluationSystem()
        self.show_question()

    # --- Show Question ---
    def show_question(self):
        for widget in self.winfo_children():
            widget.destroy()

        # End Quiz
        if self.current_question_index >= len(self.question_list):
            self.show_result()
            return

        # Current Question
        question_data = self.question_list[self.current_question_index]
        ctk.CTkLabel(self, text=question_data['question'], font=("Arial", 20)).pack(pady=20)

        # Options
        self.buttons = []
        for i, option in enumerate(question_data['options']):
            btn = ctk.CTkButton(
                self,
                text=option,
                command=lambda i=i: self.check_answer(i),
                font=("Arial", 16),
                width=500,
                height=40
            )
            btn.pack(pady=5)
            self.buttons.append(btn)

        # Timer
        self.time_left = 15
        self.timer_label = ctk.CTkLabel(self, text=f"Time Left: {self.time_left}s", font=("Arial", 18))
        self.timer_label.pack(pady=10)
        self.update_timer()

    # --- Update Timer ---
    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.configure(text=f"Time Left: {self.time_left}s")
            self.timer = self.after(1000, self.update_timer)
        else:
            self.check_answer(None)

    # --- Check Answer ---
    def check_answer(self, selected_index):
        self.after_cancel(self.timer)
        question_data = self.question_list[self.current_question_index]
        correct_index = ord(question_data['correct']) - ord('a')

        # Disable Buttons
        for btn in self.buttons:
            btn.configure(state='disabled')

        # Evaluate Answer
        user_answer = self.question_list[self.current_question_index]['options'][selected_index] if selected_index is not None else ""
        correct_answer = question_data['options'][correct_index]
        is_correct = self.evaluator.evaluate_answer(question_data['question'], user_answer, correct_answer)

        # Highlight Correct and Incorrect Answers
        if selected_index is not None:
            if is_correct:
                self.buttons[selected_index].configure(fg_color="green", text_color="white")
            else:
                self.buttons[selected_index].configure(fg_color="red", text_color="white")
                self.buttons[correct_index].configure(fg_color="green", text_color="white")
        else:
            self.buttons[correct_index].configure(fg_color="green", text_color="white")

        # Move to Next Question
        self.after(3000, self.next_question)

    # --- Next Question ---
    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    # --- Show Results ---
    def show_result(self):
        for widget in self.winfo_children():
            widget.destroy()

        # Final Score
        score_data = self.evaluator.calculate_final_score(len(self.question_list))
        feedback_summary = self.evaluator.generate_feedback_summary()

        # Display Results
        ctk.CTkLabel(self, text="Test Completed!", font=("Arial", 24)).pack(pady=20)
        ctk.CTkLabel(self, text=f"Your Score: {score_data['raw_score']}/{score_data['total_questions']} ({score_data['percentage']}%)", font=("Arial", 20)).pack(pady=10)

        # Save History
        self.evaluator.update_user_history(self.username, score_data, self.selected_category)

        # Export Results
        filename = self.evaluator.export_results(self.username, self.selected_category, score_data)
        messagebox.showinfo("Exported", f"Results saved to {filename}")

        # Feedback Summary
        ctk.CTkLabel(self, text="Feedback:", font=("Arial", 18)).pack(pady=10)
        ctk.CTkLabel(self, text=feedback_summary, font=("Arial", 14), wraplength=700).pack(pady=10)

        # Back to Categories Button
        ctk.CTkButton(
            self,
            text="Back to Categories",
            command=self.show_categories,
            font=("Arial", 18),
            width=300,
            height=50
        ).pack(pady=20)


if __name__ == "__main__":
    app = QCMApp("abdou")
    app.mainloop()
