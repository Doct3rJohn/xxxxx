# import from pyhton module (nstd)
from rich.console import Console
c = Console()

def can_i_c():
    c.print("\n[blue][*] Available modules:[/]")
    c.print("[yellow]#    Name        Description[/]")
    c.print("[red]---  ---------   ------------------------[/]")
    print("1    fakemsg     Send and created fake sms")
    print("2    header      Grab the headers of the webserver\n")

"""
def can_i_c():
    print("[*] Available modules:")
    print("#    Name        Description")
    print("---  ---------   ------------------------")
    print("1    fakemsg     Send and created fake sms")
    print("2    header      Grab the headers of the webserver\n")
"""