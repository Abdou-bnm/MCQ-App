import json
from datetime import datetime
import csv
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

class EvaluationSystem:
    def __init__(self):
        """
        Initializes the EvaluationSystem with a score and feedback list.
        """
        self.current_score = 0
        self.question_feedback = []

    def evaluate_answer(self, question, user_answer, correct_answer):
        """
        Evaluates a single answer and provides feedback with enhanced formatting.
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
        Displays enhanced feedback for each question using rich components.
        """
        if feedback['is_correct']:
            console.print(Panel("[green]✔ Correct![/green]", border_style="green"))
        else:
            console.print(Panel(
                f"[red]❌ Wrong! Your Answer: {feedback['user_answer']}[/red]\n"
                f"💡 [yellow]Correct Answer: {feedback['correct_answer']}[/yellow]",
                border_style="red"
            ))

    def calculate_final_score(self, total_questions):
        """
        Calculates and returns the final score as a percentage.
        """
        score_percentage = (self.current_score / total_questions) * 100
        return {
            "raw_score": self.current_score,
            "total_questions": total_questions,
            "percentage": round(score_percentage, 2)
        }

    def update_user_history(self, username, score, category):
        """
        Updates the user's history in the JSON file.
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
            console.print(Panel(f"[red]Error updating history: {e}[/red]", border_style="red"))
            return False

    def export_results(self, username, category, score_data):
        """
        Exports results to a CSV file with detailed feedback.
        """
        base_dir = 'data/results'
        user_dir = os.path.join(base_dir, username)

        # Create user directory if it doesn't exist
        if not os.path.exists(user_dir):
            try:
                os.makedirs(user_dir)
            except Exception as e:
                console.print(Panel(f"[red]Error creating user directory: {e}[/red]", border_style="red"))
                return None

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(user_dir, f"results_{username}_{timestamp}.csv")

        try:
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # Write metadata
                writer.writerow(['Username', 'Category', 'Date', 'Score', 'Total Questions', 'Percentage'])
                writer.writerow([
                    username,
                    category,
                    datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    score_data["raw_score"],
                    score_data["total_questions"],
                    score_data["percentage"]
                ])

                # Write detailed feedback
                writer.writerow([])
                writer.writerow(['Detailed Feedback'])
                for feedback in self.question_feedback:
                    writer.writerow([
                        feedback["question"],
                        'Correct' if feedback["is_correct"] else 'Incorrect',
                        f'Your answer: {feedback["user_answer"]}',
                        f'Correct answer: {feedback["correct_answer"]}'
                    ])
            console.print(Panel(f"[green]Results exported to: {filename}[/green]", border_style="green"))
            return filename
        except Exception as e:
            console.print(Panel(f"[red]Error exporting results: {e}[/red]", border_style="red"))
            return None