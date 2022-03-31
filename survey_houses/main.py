
# -----------------------------------------------------
# @Author 来ビス―クラム　(raibisu.kuramu@gamil.com)
# @github https://github.com/yuukuramu
# @instagram https://www.instagram.com/raibisu.kuramu
# @site https://yuukuramu.xyz
# -----------------------------------------------------

import os
import random
import json
from time import sleep

from rich import emoji
from rich.console import Console
from rich.theme import Theme
from rich.table import Table


# Color Theme: create new colour theme
custom_theme = Theme(
    {
        "error": "bold #cc0000",
        "success": "bold green",
        "attention": "bold #ff6600",
        "warning": "bold magenta",
        "option": "bold #ff0066",
        "white": "#ffffff",
    }
)

### VERIABLES

# emojies
global emojies
emojies = ["😒", "😢", "😭", "😟", "😞", "😥", "😖", "☹", "😔"]

# Dictionary
answers = {}

# Import json dictiionary
with open("questions.json") as dict:
    questions = json.load(dict)

# shortcut
console = Console(theme=custom_theme)

### FUNCTIONS
def wait(t):
    console.print("[attention][!][/] Notiek ielāde ...")
    # Sleep 2 sec! 
    sleep(t)
    console.print("[success][+][/] Ielāde veiksmīga!")
    sleep(0.5)


def clearTerminal():
    """
    Clear the terminal window
    """

    if os.name == "nt":  # posx, java, nt
        os.system("cls")
    else:
        os.system("clear")


clearTerminal()

# START - copyright PART
console.print("[attention][!][/] Lūdzu palaidiet šo skriptu konsolē, kura atbalsta UTF-8\n")
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

wait(2)
clearTerminal()

# TODO
"""
    Aptaujā parada cik % bija pozitivas atbildes cik negativas cik neitraslas
"""

### PROGRAMMA
try:
    while True:
        try:
            console.print("[option][?][/] Ievadiet cik māju aptaujās")
            house_count = int(input("=> "))

            # console.print("[option][?][/] Ievadiet mājas nummuru")
            # house = int(input("=> "))

            console.print("\n[option][?][/] Ievadiet cik dzīvokļu ir mājā")
            house_aparts_count = int(input("=> "))

            # console.print("\n[option][?][/] Ievadiet dzīvokļa nummuru")
            # house_aparts = int(input("=> "))

            console.print("\n[option][?][/] Ievadiet cik piedalās aptaujā no dzīvokļa")
            house_people = int(input("=> "))

            house_count += 1
            house_aparts_count += 1
            house_people += 1

            for house_nr in range(1, house_count):
                for a_nr in range(1, house_aparts_count):
                    for people in range(1, house_people):
                         for n in questions.keys():
    # ==================={DEBUG}===================
                            console.print(f"""
    [attention]Māja[/]: {house_nr},
    [attention]Dzīvoklis[/]: {a_nr},
    [attention]Cilvēks dzīvoklī[/]: {people},
    [attention]Jautājums[/]: {n} """)
    # ==================={DEBUG}===================
                            console.print(questions[n])
                            console.print("[white]-[/] [error](Nē)[/], [white]/[/] [warning](Pašreiz neitrāls)[/], [white]+[/] [success]Jā![/]")
                            answer = input("=> ")
                            path = f"{house_nr}/{a_nr}/{people}/{n}"
                            allowed = ["+", "-", "/"]
                            if answer in allowed:
                                answers[path] = answer
                                print(answers)

            
            console.print(f"[attention][!][/] Aptaujas rezultati!")
            for n in answers:

                global survey_results
                survey_results = n.split("/")

                h_nr = survey_results[0]
                a_nr = survey_results[1]
                person = survey_results[2]
                question = survey_results[0]

                # if int(h_nr) > 0:
                print(f"Māja {h_nr}, Dzīvoklis {a_nr}, cilvēks {person}")
                print(n, answers[n])




            break
        except ValueError:
            clearTerminal()
            console.print("[error][-][/] Atļauti tikai cipari")
            continue

except KeyboardInterrupt:

    # get random emoji from emojies liset
    emoji = random.choice(emojies)

    # GoodBye message if pressed CTRL + C
    console.print("\n\n[attention]Ceru drīz tiksimies vēlreiz [/]" + emoji)
    os.sys.exit()
