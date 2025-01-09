from user_management import UserManager
from history_tracker import HistoryTracker
from Quiz import Quiz
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align

console = Console()

def display_home():
    """
    Display the Main Menu with options only.
    """
    console.print(Panel(Align.center("📋 [bold blue]QCM Application[/bold blue]"), border_style="cyan", padding=(0, 2), width=48))  
    menu_content = "\n".join(["[bold yellow]1️⃣  🧠 Start Test[/bold yellow]", "[bold green]2️⃣  📜 View History[/bold green]", "[bold red]3️⃣  ❌ Exit[/bold red]"])  
    console.print(Panel(menu_content, title="[bold cyan]Main Menu[/bold cyan]", border_style="cyan", padding=(1, 2), width=48))  # 
    console.print("[bold cyan]💡 Enter a number to choose an option:[/bold cyan]")  


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

