from user_management import UserManager
from history_tracker import HistoryTracker
from Quiz import Quiz
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
console = Console()

def display_home():
    """
    Display the home page with options only.
    """
    console.print(Panel(Text("Options :\n1️⃣  🧠 Start MCQ Test\n2️⃣  📜 View History\n3️⃣  ❌ Exit Application", justify="left"), title="📋 [bold blue]QCM Application[/bold blue]", border_style="magenta", padding=(1, 2)))


if __name__ == "__main__":
    
    user_manager = UserManager()
    username = user_manager.get_or_create_user()
    
    while True:
        display_home()
        choice = Prompt.ask("[bold yellow]Choose an option [/bold yellow]", choices=["1", "2", "3"])

        if choice == "1":
            Quiz.start_quiz(username) 
        elif choice == "2":
            HistoryTracker.display_detailed_history(username) 
            HistoryTracker.display_result_details(username)
        elif choice == "3":
            console.print("👋 [bold yellow]Goodbye![/bold yellow] ")
            break

