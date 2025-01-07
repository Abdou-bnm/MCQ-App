import json
from datetime import datetime
import csv
import os
from rich.console import Console
from rich.text import Text

console = Console()


class EvaluationSystem:
    def __init__(self):
        self.current_score = 0
        self.question_feedback = []

    def evaluate_answer(self, question, user_answer, correct_answer):
        """
        Evaluate a single answer and provide feedback with enhanced formatting.
        """
        is_correct = user_answer == correct_answer

        feedback = {
            "question": question,
            "user_answer": user_answer,
            "correct_answer": correct_answer,
            "is_correct": is_correct
        }
        self.question_feedback.append(feedback)

        self.display_feedback(feedback)

        if is_correct:
            self.current_score += 1
        return is_correct

    def display_feedback(self, feedback):
        """
        Display enhanced feedback for each question.
        """

        # User's Answer
        if feedback['is_correct']:
            console.print(f"[green]✔ Correct! [/green]")
        else:
            console.print(f"[red]❌ Wrong! Your Answer: {feedback['user_answer']}[/red]")
            console.print(f"💡 [yellow]Correct Answer: {feedback['correct_answer']}[/yellow]\n")

    def calculate_final_score(self, total_questions):
        """
        Calculate and return the final score as a percentage.
        """
        score_percentage = (self.current_score / total_questions) * 100
        return {
            "raw_score": self.current_score,
            "total_questions": total_questions,
            "percentage": round(score_percentage, 2)
        }

    def update_user_history(self, username, score, category):
        """
        Update user's history in the JSON file.
        """
        try:
            with open('data/users.json', 'r') as file:
                users_data = json.load(file)

            if username in users_data:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                new_entry = {
                    "date": current_time,
                    "category": category,
                    "score": f"{score['raw_score']}/{score['total_questions']}"
                }
                users_data[username]["history"].append(new_entry)

                with open('data/users.json', 'w') as file:
                    json.dump(users_data, file, indent=4)
                return True
            return False
        except Exception as e:
            console.print(f"[red]Error updating history: {e}[/red]")
            return False

    def export_results(self, username, category, score_data):
        """
        Export results to a CSV file
        """
        
        base_dir = 'data/results'
        
        user_dir = os.path.join(base_dir, username)
        
        if not os.path.exists(user_dir):
            try:
                os.makedirs(user_dir)
            except Exception as e:
                print(f"Error creating user directory: {e}")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(user_dir,f"results_{username}_{timestamp}.csv")

        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Username', 'Category', 'Date', 'Score', 'Total Questions', 'Percentage'])
                writer.writerow([
                    username,
                    category,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    score_data["raw_score"],
                    score_data["total_questions"],
                    score_data["percentage"]
                ])

                writer.writerow([])
                writer.writerow(['Detailed Feedback'])
                for feedback in self.question_feedback:
                    writer.writerow([
                        feedback["question"],
                        'Correct' if feedback["is_correct"] else 'Incorrect',
                        f'Your answer: {feedback["user_answer"]}',
                        f'Correct answer: {feedback["correct_answer"]}'
                    ])
            return filename
        except Exception as e:
            console.print(f"[red]Error exporting results: {e}[/red]")
            return None
