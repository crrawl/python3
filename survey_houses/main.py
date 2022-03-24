
# -----------------------------------------------------
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------

import os
import random
import json

from rich import emoji
from rich.console import Console
from rich.theme import Theme
# from rich.table import Table

# Color Theme: create new colour theme
custom_theme = Theme(
    {
        "error": "bold red",
        "success": "bold green",
        "attention": "bold yellow",
        "warning": "bold magenta",
        "option": "violet",
        "white": "#ffffff",
    }
)

### VERIABLES

# emojies
global emojies
emojies = ["😒", "😢", "😭", "😟", "😞", "😥", "😖", "☹", "😔"]

# Import json dictiionary
with open("questions.json") as dict:
    questions = json.load(dict)

# shortcut
console = Console(theme=custom_theme)

# console.print( questions['N1'] )

### FUNCTIONS
def clearTerminal():
    """
    Clear the terminal window
    """

    if os.name == "nt":  # posx, java, nt
        os.system("cls")
    else:
        os.system("clear")



# copyright
print(
    """
----------------------------------------------------- 
@Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
@github https://github.com/yuukuramu
@instagram https://www.instagram.com/raibisu.kuramu
@site https://yuukuramu.xyz
@License -mit
-----------------------------------------------------
"""
)

console.print("[attention][!][/] lūdzu palaižat šo skriptu konsolē kura atbalsta UTF-8")

# TODO
"""
    Aptaujā parada cik % bija pozitivas atbildes cik negativas cik neitraslas
"""

### PROGRAMMA
try:
    while True:
        console.print("[option][?][/] Ievadiet mājas, dzīvokļa nummuru un cik piedalās aptaujā no dzīvokļa \nPiemērs: 2, 3, 2")
        try:
            house = [int(n) for n in input("=> ").split(',')]
            console.print("[option][?][/] Cik no dzīvokļa piedalās aptaujā")
            
            # for i in range(house[2]):
                

        except ValueError:
            console.print("[error][-][/] Atļauti tikai cipari")
            continue

        print(house)
        console.print(f"""[success][+][/] Jūsu mājas nummurs: {house[0]}, dzīvokļa nummurs: {house[1]}""")
        
        break
except KeyboardInterrupt:

    # get random emoji from emojies liset
    emoji = random.choice(emojies)

    # GoodBye message if pressed CTRL + C
    console.print("\n[attention]Ceru drīz tiksimies vēlreiz [/]" + emoji)
    os.sys.exit()