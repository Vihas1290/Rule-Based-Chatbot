import rich
import time
import random
from rich import print as rprint
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, track

rprint("[bold green]Hello User![/bold green]")

console = Console()
console.print("Welcome to [bold blue]RichTest[/bold blue]!", style="bold magenta")

table = Table(title="Rich Test Table", header_style="bold blue")
table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Age", style="magenta")
table.add_column("City", style="green")

table.add_row("Alice", "30", "New York")
table.add_row("Bob", "25", "Los Angeles")
table.add_row("Charlie", "35", "Chicago")
table.add_row("Berbert", "14", "Hyderabad")

console.print(table)

for i in track(range(100), description="Processing..."): 
    time.sleep(random.random()/5)