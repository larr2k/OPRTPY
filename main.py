import argparse
from rich.console import Console
from modules import name_lookup, plate_lookup, address_lookup

console = Console()

def banner():
    console.print("[bold cyan]People OSINT Tool v1.0[/bold cyan]", justify="center")
    console.print("[bold green]by YOU[/bold green]\n", justify="center")

def main():
    banner()
    
    parser = argparse.ArgumentParser(description="OSINT CLI for People Search")
    subparsers = parser.add_subparsers(dest="command")

    # Name Search
    name_parser = subparsers.add_parser("name", help="Search for a person by name")
    name_parser.add_argument("full_name", type=str, help="Full name of the person")

    # License Plate Search
    plate_parser = subparsers.add_parser("plate", help="Search by license plate")
    plate_parser.add_argument("plate_number", type=str, help="License plate number")
    plate_parser.add_argument("state", type=str, help="State (e.g., CA, TX)")

    # Address Search
    address_parser = subparsers.add_parser("address", help="Search for public data on an address")
    address_parser.add_argument("address", type=str, help="Street address")

    args = parser.parse_args()

    if args.command == "name":
        name_lookup.search(args.full_name)
    elif args.command == "plate":
        plate_lookup.search(args.plate_number, args.state)
    elif args.command == "address":
        address_lookup.search(args.address)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
