#!/usr/bin/env python3
# date: 10/8/2022

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
    print("set          Set the values                  <number> <message> <key>")
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
    print(" NUMBER          yes         The target phone number, must use the [country code]")
    print(" MESSAGE         yes         The message that be send to the target")
    print(" KEY             no          The [default]:key, let you send one message per day. However, you can buy it here: https://textbelt.com/\n")

# Convert string into list
def string2list(string):
    return(list(string.split(" ")))

# Convert list into string
def list2string(list):
    return(" ".join(list))

# Setting up values into variable
def sit_up(string, values):
    global num
    global msg
    global key

    match string.lower():
        case "number":
            num = values

            # error handling:
            # looking for spaces/empty at the start/first arguments
            if not num[0]:
                c.print("[red]SpacesError:[/] first arguments cannot be spaces")
            else:
                print(f"NUMBER -> {num[0]}")          
 
        case "message":
            msg = list2string(values)

            # error handling:
            # looking for spaces/empty at the start/first arguments
            gather_list = list(msg)
            chosen_1 = gather_list[0]
            if chosen_1 == ' ':
                c.print("[red]SpacesError:[/] first arguments cannot be spaces")
            else:
                print(f"MESSAGE -> {msg}")

        case "key":
            key = values

            # error handling:
            # looking for spaces/empty at the start/first arguments
            if not key[0]:
                c.print("[red]SpacesError:[/] first arguments cannot be spaces")  
            else:            
                print(f"KEY -> {key[0]}")

def run(number, message, key=string2list("textbelt")):
    SUCCESS = b'"success":true'
    FAILED = b'"success":false'

    c.print("[blue][*][/] Running the modules...")
    c.print("[blue][*][/] Compiling the message...")
    c.print(f"[blue][*][/] Send the message over '{list2string(number)}'")

    # where the request handling
    data = {'phone':f'{list2string(number)}', 'message':f'{message}', 'key':f'{list2string(key)}'}
    resp = requests.post("https://textbelt.com/text", data=data)
    if SUCCESS in resp.content:
        c.print("[green][+][/] Module execution completed")
    elif FAILED in resp.content:
        c.print("[red][!][/] Cannot execute the modules > quotaRemaining:0")
    else:
        c.print("[red]Error:[/] something went wrong")

# Seriously, I need help!
def fakemsg():
    while True:
        try:
            petai_prompt = c.input("[underline]petai[/] ([green]osint/modules/fakemsg[/]) > ")
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
                    if key != None:
                        run(num, msg, key)
                    else:
                        run(num, msg)
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
    fakemsg()
