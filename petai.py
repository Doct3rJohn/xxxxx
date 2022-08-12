#!/usr/bin/env python3

# import from python module (std)
import sys
from os import system, name

# import from pyhton module (nstd)
from rich.console import Console
c = Console()

# import from custom module
from bridge import gimme_this
from imdead import can_i_c

AUTHOR = "Shafiq Aiman"
VERSION = "v0.1"

# just print the banner
# you know, to look cool! lol
def show_off():
    print("(((_.-=-._.-=-._.-=-)))")
    print(" ))~~~~~~~~~~~~~~~~~(( ") 
    c.print("(( >[green]PETAI-FRAMEWORK[/]< ))")
    print(" )).................(( ")
    print("(((`-._.-'`-._.-'`-.)))")
    c.print("[red]_______________________[/]")
    c.print(f"Petai-Framework: [yellow]{VERSION}[/]")
    c.print(f"Author: [yellow]{AUTHOR}[/]\n")

def need_help():
    c.print("\n[blue][*] Available commands:[/]")
    c.print("[yellow]Command      Description                 Arguments[/]")
    c.print("[red]--------     -----------                 ------------[/]")
    print("help         Help menu")
    print("use          Interact with a module      <#> | <name>")
    print("show         Displays all modules")
    print("version      Show the version")
    print("clear        Clear the screen")
    print("exit         Exit the console\n")

# convert string to list
def string2list(string):
    return(list(string.split(" ")))

def main():
    show_off()
    while True:
        try:
            petai_prompt = c.input("[underline]petai[/] > ")
            petai_prompt = string2list(petai_prompt)
            # error handling:
            # looking for spaces/empty at the start/first arguments
            #if not petai_prompt[0]:
            #    print("SpacesError: first arguments cannot be spaces")
            #else:
            match petai_prompt[0].lower():
                case "use":
                    # error handling:
                    # if [use] doesn't have arguments. Boo 2 the user
                    try:
                        gimme_this(petai_prompt[1].lower())
                    except IndexError:
                        c.print("[red]ArgumentError:[/] must have an arguments")
                case "show":
                    can_i_c()
                case "help":
                    need_help()
                case "version":
                    print(f"Petai-Framework: {VERSION}")
                case "clear":
                    if name == 'nt':
                        _ = system('cls')
                    else:
                        _ = system('clear')
                case "exit" | "quit":
                    sys.exit(0)
                case "": 
                    # press enter the prompt went down. Down there!?
                    continue
                case _:
                    c.print(f"[red]Error[/]: unknown command")
        except KeyboardInterrupt:
            c.print(" [red]Interrupt:[/] use the 'exit' command to quit")
            continue

if __name__ == "__main__":
    main()