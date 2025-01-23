import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os
import csv

console = Console()

class HistoryTracker:
    FILE_PATH = "data/users.json"
    RESULT_DIR = ""
    
    @staticmethod
    def username_dir(username):
        HistoryTracker.RESULT_DIR = f"data/results/{username}"
        
    @staticmethod
    def display_detailed_history(username):
        with open(HistoryTracker.FILE_PATH, 'r') as file:
            users = json.load(file)

        if username not in users or not users[username].get("history"):
            console.print(f"😔 [red]No history found for user: {username}[/red]")
            return

        # Display history as a table
        table = Table(title=Panel(f"📜 {username}'s History", border_style="blue"))
        table.add_column("📅 Date", style="cyan")
        table.add_column("📚 Category", style="magenta")
        table.add_column("✅ Score", style="green")

        for record in users[username]["history"]:
            table.add_row(record["date"], record["category"], record["score"])

        console.print(table)

    @staticmethod
    def display_result_details(username):
        HistoryTracker.username_dir(username)
        result_files = [f for f in os.listdir(HistoryTracker.RESULT_DIR) if f.startswith(f"results_{username}_") and f.endswith('.csv')]
        if not result_files:
            console.print(Panel("😔 [red]No previous results found.[/red]", border_style="blue"))
            input("**Press any key to return to home page**")
            console.print(Panel("🏠 [bold yellow]Returning to home page...[/bold yellow]", border_style="yellow"))
            return

        console.print(Panel("[bold yellow]📁 Available Tests:[/bold yellow]", border_style="blue",width=48))
        console.print("0. [bold red] Return to home page [/bold red]")
        for idx, file in enumerate(result_files, 1):
            console.print(f"{idx}. 📄 {file}")

        try:
            choice = int(console.input("[bold blue]Select a test to view details (number): [/bold blue]"))
            if choice == 0 :
                return
            selected_file = result_files[choice - 1]
        except (IndexError, ValueError):
            console.print("❌ [red]Invalid selection. Returning to menu.[/red]")
            return

        file_path = os.path.join(HistoryTracker.RESULT_DIR, selected_file)
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            metadata = rows[1]  
            console.print("\n[bold cyan]📋 Test Details:[/bold cyan]")
            console.print(f"👤 [bold]Username:[/bold] {metadata[0]}")
            console.print(f"📚 [bold]Category:[/bold] {metadata[1]}")
            console.print(f"📅 [bold]Date:[/bold] {metadata[2]}")
            console.print(f"✅ [bold]Score:[/bold] {metadata[3]}/{metadata[4]} ({metadata[5]}%)\n")

            console.print("[bold cyan]📝 Question Details:[/bold cyan]\n")
            result_table = Table(title="📝 Quiz Results")
            result_table.add_column("📋 Question", style="cyan", overflow="fold")
            result_table.add_column("❓ Your Answer", style="magenta")
            result_table.add_column("✅ Correct Answer", style="green")
            result_table.add_column("✔ Result", style="yellow")

            start_feedback = False
            for row in rows:
                if not row:
                    continue
                
                if "Detailed Feedback" in row[0]:
                    start_feedback = True
                    continue
                
                if start_feedback:  # Only process feedback rows
                    question = row[0]
                    result = row[1]
                    user_answer = row[2].replace("Your answer: ", "") if len(row) > 2 else "N/A"
                    correct_answer = row[3].replace("Correct answer: ", "") if len(row) > 3 else "N/A"

                    emoji = "✅" if result == "Correct" else "❌"
                    result_table.add_row(question, user_answer, correct_answer, emoji)

            console.print(result_table)
            
            input("**Press any key to return to home page**")
            console.print(Panel("🏠 [bold yellow]Returning to Main Menu...[/bold yellow]", border_style="yellow",width=48))
