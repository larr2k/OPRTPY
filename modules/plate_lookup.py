import requests
from rich.console import Console

console = Console()

def search(plate_number, state):
    console.print(f"[bold yellow]Searching for plate:[/bold yellow] {plate_number} in {state}")

    try:
        url = f"https://some-license-plate-api.com/search?plate={plate_number}&state={state}"
        response = requests.get(url)

        if response.status_code == 200:
            console.print(response.json())  # Print results
        else:
            console.print("[bold red]No results found or API error.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
