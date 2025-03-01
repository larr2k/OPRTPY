import requests
from rich.console import Console

console = Console()

def search(full_name):
    console.print(f"[bold yellow]Searching for:[/bold yellow] {full_name}")

    try:
        # Example: Searching a people search API
        url = f"https://some-people-search-api.com/search?name={full_name}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            console.print(data)  # Print structured data
        else:
            console.print("[bold red]No results found or API error.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
