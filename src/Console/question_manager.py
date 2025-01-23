import json
from rich.console import Console

console = Console()

class QuestionManager:
    FILE_PATH = "data/questions_1.json"

    def __init__(self):
        """
        Initializes the QuestionManager by loading questions from the JSON file.
        """
        self.questions_data = None
        try:
            with open(self.FILE_PATH, 'r') as file:
                self.questions_data = json.load(file)
        except FileNotFoundError:
            console.print(f"[red]Error: Questions file '{self.FILE_PATH}' not found.[/red]")
        except json.JSONDecodeError:
            console.print(f"[red]Error: Failed to decode '{self.FILE_PATH}'. Please check the file format.[/red]")
        except Exception as e:
            console.print(f"[red]Unexpected error while loading questions: {e}[/red]")

    def select_category(self):
        """
        Prompts the user to select a category or go back to the main menu.
        """
        if not self.questions_data or 'categories' not in self.questions_data:
            console.print("[red]No categories found in the questions file.[/red]")
            return None

        categories = [category['name'] for category in self.questions_data['categories']]
        if not categories:
            console.print("[red]No categories available.[/red]")
            return None

        console.print("\n[bold cyan]Available Categories:[/bold cyan]")
        for idx, category in enumerate(categories, 1):
            console.print(f"{idx}. {category}")
        console.print("[bold red]0. 🏠 Return to Main Menu[/bold red]")

        while True:
            try:
                choice = console.input("[bold blue]Select a category (number): [/bold blue]")
                if choice == "0":  # Return to main menu
                    return None
                choice = int(choice) - 1
                if 0 <= choice < len(categories):
                    return categories[choice]
                else:
                    console.print("[red]Invalid choice. Please select a valid number.[/red]")
            except ValueError:
                console.print("[red]Invalid input. Please enter a number.[/red]")

    def select_level(self, category):
        """
        Prompts the user to select a level or go back to the category selection.
        """
        if not self.questions_data or 'categories' not in self.questions_data:
            console.print("[red]No categories found in the questions file.[/red]")
            return None

        for cat in self.questions_data['categories']:
            if cat['name'] == category:
                levels = [lvl['level'] for lvl in cat.get('levels', [])]
                if not levels:
                    console.print(f"[red]No levels found for category '{category}'.[/red]")
                    return None

                console.print("\n[bold cyan]Available Levels:[/bold cyan]")
                for idx, lvl in enumerate(levels, 1):
                    console.print(f"{idx}. {lvl}")
                console.print("[bold red]0. ↩ Return to Category Selection[/bold red]")
                console.print("[bold red]00. 🏠 Return to Main Menu[/bold red]")

                while True:
                    try:
                        choice = console.input("[bold blue]Select a level (number): [/bold blue]")
                        if choice == "0":  # Go back to category selection
                            return "back"  # Return "back" to indicate category selection
                        if choice == "00":  # Go back to main menu
                            return None  # Return None to indicate main menu
                        choice = int(choice) - 1
                        if 0 <= choice < len(levels):
                            return levels[choice]
                        else:
                            console.print("[red]Invalid choice. Please select a valid number.[/red]")
                    except ValueError:
                        console.print("[red]Invalid input. Please enter a number.[/red]")

        console.print(f"[red]Category '{category}' not found.[/red]")
        return None

    def get_questions(self, category, level):
        """
        Retrieves the questions for the selected category and level.
        """
        if not self.questions_data or 'categories' not in self.questions_data:
            console.print("[red]No categories found in the questions file.[/red]")
            return None

        for cat in self.questions_data['categories']:
            if cat['name'] == category:
                for lvl in cat.get('levels', []):
                    if lvl['level'] == level:
                        return lvl.get('questions', [])

        console.print(f"[red]No questions found for category '{category}' and level '{level}'.[/red]")
        return None