import requests
from rich.console import Console

console = Console()

def search(address):
    console.print(f"[bold yellow]Searching for address:[/bold yellow] {address}")

    try:
        url = f"https://some-address-api.com/search?address={address.replace(' ', '+')}"
        response = requests.get(url)

        if response.status_code == 200:
            console.print(response.json())  # Print results
        else:
            console.print("[bold red]No results found or API error.[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
