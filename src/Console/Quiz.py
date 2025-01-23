from question_manager import QuestionManager
from evaluation_system import EvaluationSystem
from timer_check import QuizTimer
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.align import Align
import time

console = Console()

# Time limits for each difficulty level
LEVEL_TIMES = {
    "easy": 30,    # 30 seconds
    "medium": 20,  # 20 seconds
    "hard": 10     # 10 seconds
}

class Quiz:
    @staticmethod
    def start_quiz(username):
        """
        Starts the quiz for the given username with navigation options.
        """
        try:
            q_manager = QuestionManager()
            evaluator = EvaluationSystem()

            # Select category
            category = q_manager.select_category()
            if not category:  # User chose to return to main menu
                console.print("[yellow]Returning to the main menu...[/yellow]")
                return  # Exit the quiz and return to the main menu

            # Select difficulty level
            level = q_manager.select_level(category)
            if level == "back":  # User chose to return to category selection
                Quiz.start_quiz(username)  # Restart quiz to select a new category
                return
            if level is None:  # User chose to return to main menu
                console.print("[yellow]Returning to the main menu...[/yellow]")
                return

            # Get questions for the selected category and level
            questions = q_manager.get_questions(category, level)
            if not questions:
                console.print(f"[red]No questions available for {category} - {level} level.[/red]")
                return

            console.print(Panel(f"🚀 [bold green]Starting quiz in {category} - {level} level[/bold green]", style="green"))

            # Initialize score data
            score_data = {
                'raw_score': 0,
                'total_questions': len(questions),
                'percentage': 0.0
            }

            # Iterate through questions
            idx = 0
            while idx < len(questions):
                question = questions[idx]
                try:
                    # Display the question
                    console.print(Panel(f"❓ [bold yellow]Question {idx + 1}: {question['question']}[/bold yellow]", style="yellow"))
                    for i, option in enumerate(question['options'], 1):
                        console.print(f"{i}. {option}")
                    console.print("[bold red]0. 🏠 Return to Main Menu[/bold red]")

                    # Start the timer
                    timer = QuizTimer(level.lower())
                    timer.start_timer()

                    # Get user's answer
                    user_answer = None
                    while not timer.is_time_up():
                        try:
                            user_answer = Prompt.ask("[bold blue]Select your answer [/bold blue]")
                            if user_answer == "0":  # Return to main menu
                                confirm = Prompt.ask("[bold red]Are you sure you want to return to the main menu? (y/n): [/bold red]")
                                if confirm.lower() == 'y':
                                    console.print("[yellow]Returning to the main menu...[/yellow]")
                                    return
                                else:
                                    continue
                            if not user_answer.isdigit() or int(user_answer) < 1 or int(user_answer) > len(question['options']):
                                raise ValueError("Invalid answer")
                            break
                        except ValueError:
                            console.print("[red]Invalid answer. Try again![/red]")

                    if timer.is_time_up():
                        console.print("[red]Time's up! Moving to the next question...[/red]")
                        idx += 1
                        continue

                    # Evaluate the answer if provided
                    if user_answer and user_answer != "0":
                        is_correct = evaluator.evaluate_answer(
                            question['question'],
                            question['options'][int(user_answer) - 1],
                            question['options'][question['correct']]
                        )
                        if is_correct:
                            score_data['raw_score'] += 1
                        idx += 1  # Move to the next question

                except Exception as e:
                    console.print(f"[red]An error occurred while processing the question: {e}[/red]")

            # Calculate final score
            score_data['percentage'] = (score_data['raw_score'] / score_data['total_questions']) * 100
            Quiz.display_final_score(username, category, score_data)

            # Update user history and export results
            evaluator.update_user_history(username, score_data, category)
            evaluator.export_results(username, category, score_data)

        except Exception as e:
            console.print(f"[red]Unexpected error during the quiz: {e}[/red]")
        finally:
            # Only show the "Returning to home page" message if the quiz was completed or an error occurred
            if 'questions' in locals() and questions:  # type: ignore 
                console.print(Panel("🏠 [bold yellow]Returning to home page...[/bold yellow]", style="yellow"))

    @staticmethod
    def display_final_score(username, category, score_data):
        """
        Displays the final score after the quiz.
        """
        console.print("\n🏆 [bold green]Test Completed![/bold green] 🏆")
        console.print(f"👤 [bold cyan]Username:[/bold cyan] {username}")
        console.print(f"📚 [bold cyan]Category:[/bold cyan] {category}")
        console.print(f"✅ [bold cyan]Score:[/bold cyan] {score_data['raw_score']}/{score_data['total_questions']} "
                      f"({score_data['percentage']:.2f}%)\n")