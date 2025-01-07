from question_manager import QuestionManager
from evaluation_system import EvaluationSystem
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
console = Console()


class Quiz:
    @staticmethod
    def start_quiz(username):
        """
        Start the quiz process.
        """
        q_manager = QuestionManager()
        evaluator = EvaluationSystem()

        category = q_manager.select_category()
        level = q_manager.select_level(category)
        questions = q_manager.get_questions(category, level)

        console.print(Panel(f"🚀 [bold green]Starting quiz in {category} - {level} level[/bold green]",border_style="green"))

        for idx, question in enumerate(questions, 1):
            console.print(Panel(f"❓ [bold yellow]Question {idx}: {question['question']}[/bold yellow]",border_style="yellow"))
            for i, option in enumerate(question['options']):
                console.print(f"{i + 1}. {option}")

            while True:
                try:
                    user_answer = int(Prompt.ask("[bold blue]Your answer (number): [/bold blue]")) - 1
                    if 0 <= user_answer < len(question['options']):
                        break  # Valid input, exit loop
                    else:
                        console.print("[red]❌ Invalid option. Choose a valid number![/red]")
                except ValueError:
                    console.print("[red]❌ Invalid input. Enter a number![/red]")

            evaluator.evaluate_answer(
                question['question'], 
                question['options'][user_answer], 
                question['options'][question['correct']]
            )

        score_data = evaluator.calculate_final_score(len(questions))

        Quiz.display_final_score(username, category, score_data)

        evaluator.update_user_history(username, score_data, category)
        evaluator.export_results(username, category, score_data)
        
        input("**Press any key to return to home page**")
        console.print(Panel("🏠 [bold yellow]Returning to home page...[/bold yellow]", border_style="yellow"))
        console.clear()

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
