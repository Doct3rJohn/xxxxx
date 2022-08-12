# import from custom module
from osint.fakemsg import fakemsg

# import from pyhton module (nstd)
from rich.console import Console
c = Console()

def gimme_this(id):
    match id:
        case "1" | "fakemsg":
            fakemsg()
        case _:
            c.print("[red]Error:[/] modules doesn't exist")