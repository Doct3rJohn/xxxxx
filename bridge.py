# import from custom module
from osint.fakemsg import fakemsg

def gimme_this(id):
    match id:
        case "1" | "fakemsg":
            fakemsg()
        case _:
            print("can't find the modules")