from user_management import UserManager
from history_tracker import HistoryTracker
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.align import Align
from Quiz import Quiz

console = Console()

def display_home():
    """
    Displays the main menu of the QCM application.
    """
    console.print(Panel(Align.center("📋 [bold blue]QCM Application[/bold blue]"), border_style="cyan", padding=(0, 2), width=48))
    menu_content = "\n".join([
        "[bold yellow]1️⃣  🧠 Start Test[/bold yellow]",
        "[bold green]2️⃣  📜 View History[/bold green]",
        "[bold red]3️⃣  ❌ Exit[/bold red]"
    ])
    console.print(Panel(menu_content, title="[bold cyan]Main Menu[/bold cyan]", border_style="cyan", padding=(1, 2), width=48))
    console.print("[bold cyan]💡 Enter a number to choose an option:[/bold cyan]")

def handle_menu_choice(choice, username):
    """
    Handles the user's menu choice.
    """
    if choice == "1":
        Quiz.start_quiz(username)
    elif choice == "2":
        HistoryTracker.display_detailed_history(username)
        HistoryTracker.display_result_details(username)
    elif choice == "3":
        console.print("👋 [bold yellow]Goodbye![/bold yellow]")
        return False  # Exit the loop
    return True  # Continue the loop

def main():
    """
    Main function to run the QCM application.
    """
    try:
        # Initialize UserManager and get/create user
        user_manager = UserManager()
        username = user_manager.get_or_create_user()

        # Main application loop
        while True:
            try:
                display_home()
                choice = Prompt.ask("[bold yellow]Choose an option [/bold yellow]", choices=["1", "2", "3"])
                if not handle_menu_choice(choice, username):
                    break  # Exit the application
            except KeyboardInterrupt:
                console.print("\n[red]Operation cancelled by the user. Returning to the main menu...[/red]")
            except Exception as e:
                console.print(f"[red]Error: {e}. Returning to the main menu...[/red]")
    except Exception as e:
        console.print(f"[red]Critical error occurred: {e}. Exiting application.[/red]")
    finally:
        console.print(Panel("👋 [bold yellow]Thank you for using the QCM Application![/bold yellow]", border_style="yellow"))

if __name__ == "__main__":
    main()