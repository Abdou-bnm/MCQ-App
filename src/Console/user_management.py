import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from history_tracker import HistoryTracker

console = Console()

class UserManager:
    FILE_PATH = "data/users.json"

    def __init__(self):
        """
        Initializes the UserManager and ensures the users file exists.
        """
        try:
            if not os.path.exists(self.FILE_PATH):
                with open(self.FILE_PATH, 'w') as file:
                    json.dump({}, file)
        except Exception as e:
            console.print(f"[red]Error initializing user data file: {e}[/red]")

    def get_or_create_user(self):
        """
        Gets or creates a user profile and displays their history upon login.
        """
        try:
            username = console.input("[bold green]Enter your username: [/bold green]").strip()
            with open(self.FILE_PATH, 'r') as file:
                users = json.load(file)

            if username not in users:
                console.print("[yellow]New user detected. Creating profile...[/yellow]")
                users[username] = {"role": "student", "history": []}
                with open(self.FILE_PATH, 'w') as file:
                    json.dump(users, file, indent=4)
                folder_path = os.path.join("data", "results", username)
                os.makedirs(folder_path, exist_ok=True)
            else:
                console.print(Panel(Align.center(f"[bold cyan]🌟 Welcome back, {username}! 🌟[/bold cyan]"), border_style="blue", width=48))
                # Display the user's history immediately after login
                HistoryTracker.display_detailed_history(username)

            return username
        except json.JSONDecodeError:
            console.print("[red]Error decoding users.json. Please check the file format.[/red]")
        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")