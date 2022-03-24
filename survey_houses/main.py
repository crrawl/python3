
# -----------------------------------------------------
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------

from multiprocessing.sharedctypes import Value
import os
# import sys
import random

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
        "blocked": "#383B40",
    }
)

### VERIABLES

# emojies
global emojies
emojies = ["😒", "😢", "😭", "😟", "😞", "😥", "😖", "☹", "😔"]

# shortcut
console = Console(theme=custom_theme)

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
        console.print("[option][?][/] Ievadiet mājas un dzīvokļa nummuru \nPiemērs: 2, 3")
        try:
            house = [int(n) for n in input("=> ").split(',')]
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