from question_manager import QuestionManager
from evaluation_system import EvaluationSystem
from timer import QuizTimer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
import time

console = Console()

class Quiz:
    @staticmethod
    def start_quiz(username):
        try:
            q_manager = QuestionManager()
            evaluator = EvaluationSystem()

            category = q_manager.select_category()
            if not category:
                console.print("[red]No category selected. Returning to main menu.[/red]")
                return

            level = q_manager.select_level(category)
            questions = q_manager.get_questions(category, level)
            if not questions:
                console.print(f"[red]No questions available for {category} - {level} level.[/red]")
                return

            console.print(Panel(Align.center(f"🚀 [bold green]Starting quiz in {category} - {level} level[/bold green]"), border_style="green"))
            
            for idx, question in enumerate(questions, 1):
                try:
                    console.print(Panel(Align.center(f"❓ [bold yellow]Question {idx}: {question['question']}[/bold yellow]"), border_style="yellow"))
                    for i, option in enumerate(question['options']):
                        console.print(f"{i + 1}. {option}")

                    user_answer = Prompt.ask("[bold blue]Your answer (number): [/bold blue]")
                    evaluator.evaluate_answer(
                        question['question'],
                        question['options'][int(user_answer) - 1],
                        question['options'][question['correct']]
                    )
                except (ValueError, IndexError):
                    console.print("[red]Invalid answer. Moving to the next question...[/red]")

            score_data = evaluator.calculate_final_score(len(questions))
            Quiz.display_final_score(username, category, score_data)
        except Exception as e:
            console.print(f"[red]Unexpected error during the quiz: {e}[/red]")

        evaluator.update_user_history(username, score_data, category)
        evaluator.export_results(username, category, score_data)

        input("**Press any key to return to the home page**")
        console.print(Panel("🏠 [bold yellow]Returning to home page...[/bold yellow]", border_style="yellow"))

    @staticmethod
    def display_final_score(username, category, score_data):
        """
        Display the final score after the test.
        """
        console.print("\n🏆 [bold green]Test Completed![/bold green] 🏆")
        console.print(f"👤 [bold cyan]Username:[/bold cyan] {username}")
        console.print(f"📚 [bold cyan]Category:[/bold cyan] {category}")
        console.print(f"✅ [bold cyan]Score:[/bold cyan] {score_data['raw_score']}/{score_data['total_questions']} "
                      f"({score_data['percentage']}%)\n")
