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
        if not os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'w') as file:
                json.dump({}, file)

    def get_or_create_user(self):
        username = console.input("[bold green]Enter your username: [/bold green]").strip()
        with open(self.FILE_PATH, 'r') as file:
            users = json.load(file)

        if username not in users:
            console.print("[yellow]New user detected. Creating profile...[/yellow]")
            users[username] = {"history": []}
            with open(self.FILE_PATH, 'w') as file:
                json.dump(users, file, indent=4)
        else:
            console.print(Panel(Align.center(f"[bold cyan]🌟 Welcome back, {username}! 🌟[/bold cyan]"), border_style="blue"))
        return username

        

