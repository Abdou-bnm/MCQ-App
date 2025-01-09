import json
from rich.console import Console
console = Console()

class QuestionManager:
    FILE_PATH = "data/questions_1.json"

    def __init__(self):
        with open(self.FILE_PATH, 'r') as file:
            self.questions_data = json.load(file)

    def select_category(self):
        console.print("\n[bold cyan]Available Categories:[/bold cyan]")
        categories = [category['name'] for category in self.questions_data['categories']]
        for idx, category in enumerate(categories, 1):
            console.print(f"{idx}. {category}")

        while True:
            try:
                choice = int(console.input("[bold blue]Select a category (number): [/bold blue]")) - 1
                if 0 <= choice < len(categories):
                    return categories[choice]
            except ValueError:
                console.print("[red]Invalid input. Try again![/red]")

    def select_level(self, category):
        for cat in self.questions_data['categories']:
            if cat['name'] == category:
                console.print("\n[bold cyan]Available Levels:[/bold cyan]")
                levels = [lvl['level'] for lvl in cat['levels']]
                for idx, lvl in enumerate(levels, 1):
                    console.print(f"{idx}. {lvl}")
                while True:
                    try:
                        choice = int(console.input("[bold blue]Select a level (number): [/bold blue]")) - 1
                        if 0 <= choice < len(levels):
                            return levels[choice]
                    except ValueError:
                        console.print("[red]Invalid input. Try again![/red]")

    def get_questions(self, category, level):
        for cat in self.questions_data['categories']:
            if cat['name'] == category:
                for lvl in cat['levels']:
                    if lvl['level'] == level:
                        return lvl['questions']
