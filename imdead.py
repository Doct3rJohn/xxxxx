# import from pyhton module (nstd)
from rich.console import Console
c = Console()

def can_i_c():
    c.print("\n[blue][*] Available modules:[/]")
    c.print("[yellow]#    Name        Description[/]")
    c.print("[red]---  ---------   ------------------------[/]")
    print("1    fakemsg     Send and Create Fake SMS\n")