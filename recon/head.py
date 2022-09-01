#!/usr/bin/env python3
# date: 12/8/2022

# import from python module (std)
from os import system, name
import sys
import requests

# import from pyhton module (nstd)
from rich.console import Console
c = Console()

def need_help():
    c.print("\n[blue][*] Available commands:[/]")
    c.print("[yellow]Command      Description                     Arguments[/]")
    c.print("[red]--------     ---------------------------     ------------------------[/]")
    print("set          Set the values                  <target> <port>")
    print("options      Displays the module option")
    print("help         Help menu")
    print("clear        Clear the screen")
    print("exit         Go to the main menu")
    print("quit         Quit\n")

def option4what():
    print("")
    c.print("[blue][*] Module options:[/]")
    c.print("[yellow] Name            Required    Description[/]")
    c.print("[red] --------        --------    --------------------------------------------------------[/]")
    print(" TARGET          yes         The URL of the target")
    print(" PORT            yes         The port of the target host\n")

# Convert string into list
def string2list(string):
    return(list(string.split(" ")))

# Convert list into string
def list2string(list):
    return(" ".join(list))

# Setting up values into variable
def sit_up(string, values):
    global target
    global port
    port = None

    match string.lower():
        case "target":
            target = values

            # error handling:
            # looking for spaces/empty at the start/first arguments
            if not target[0]:
                c.print("[red]SpacesError:[/] first arguments cannot be spaces")
            else:
                print(f"TARGET -> {target[0]}")          

        case "port":
            port = list2string(values)

            # error handling:
            # looking for spaces/empty at the start/first arguments
            if not port[0]:
                c.print("[red]SpacesError:[/] first arguments cannot be spaces")  
            else:            
                print(f"PORT -> {[port][0]}")

def run(target, port="80"):
    req = requests.head(f"{list2string(target)}:{port}")
    resp = req.headers
    for key, value in resp.items():
        print(f"{key}: {value}")

# Seriously, I need help!
def head_header():
    while True:
        try:
            petai_prompt = c.input("[underline]petai[/] ([green]recon/modules/header[/]) > ")
            petai_prompt = string2list(petai_prompt)

            # error handling:
            # looking for spaces/empty at the start/first arguments
            #if not petai_prompt[0]:
            #    print("SpacesError: first arguments cannot be spaces")
            #else:
            match petai_prompt[0].lower():
                case "set":
                    sit_up(petai_prompt[1], petai_prompt[2:])
                case "run":
                    if port != None:
                        run(target, port)
                    else:
                        run(target)
                case "options":
                    # run the options[function]
                    # but it is electric static
                    option4what()
                case "help":
                    need_help()
                case "clear":
                    if name == 'nt':
                        _ = system('cls')
                    else:
                        _ = system('clear')
                case "exit":
                    break
                case "quit":
                    sys.exit(0)
                case "":
                    continue
                case _:
                    c.print(f"[red]Error[/]: unknown command")
        except IndexError:
            c.print("[red]ArgumentError:[/] must have an arguments")
        except NameError:
            c.print("[red]Error:[/] something went wrong")
        except KeyboardInterrupt:
            c.print(" [red]Interrupt:[/] use 'exit' to go the main menu, use 'quit' to quit")
            continue

if __name__ == "__main__":
    head_header()

