from logging import error
import os
import time
import json


from rich.console import Console
from rich.theme import Theme
from rich.table import Table

# Color Theme: create new colour theme
custom_theme = Theme({  "error" : "bold red", 
                        "success" : "bold green", 
                        "attention" : "bold yellow", 
                        "warning" : "bold magenta",
                        "option" : "#4169E1",
                        })

# shortcut
console = Console(theme=custom_theme)



''' 
Pārbauda, kāda operētājsistēma ir lietotājam
skatoties no rezultāta izvadas attiecīga komanda
'''
if os.name == "nt": # posx, java, nt
    os.system("cls")
else:
    os.system("clear")
# points
points = 0
# Dictionary answers
answers = {
    "PHP": {
        
    }
}
# Import json dictiionary
with open('dictionary.json') as dict:
  questions = json.load(dict)

# Sey to user, how to quit from app
console.print(">> Iziet no programmas var ar kombināciju (Ctrl + C)", style="bold white")

# introduction
console.print(questions["start"]["WELCOME"])

# Turn eneter to continiune
input()  


# requiring a name
current_username = str(input("Ievadiet savu vārdu => ")) 

# requiring user to enter skills
console.print(questions["start"]["question"]["N1"])

# Enter a skills key then split on "," char 
PSkills = str(input("Atbildi ievadiet ar ','. Piemērs a,e => ")).replace(" ","").lower().split(",")

# print(PSkills) # print entered skills. TIMED FUNC

'''
The loop goes through all the elements of PSkills, then in the perpetual loop it is checked 
whether the entered element in PSkills coincides with some element from the dictionary.
If it matches, it is output and saved if no error is displayed
'''
for ikey in PSkills:
    while True:
        if ikey in questions["skills"].keys():
            console.print(ikey + ": Jūs izvēlējāties " + questions["skills"][ikey], style="success")
            break

        elif ikey not in questions["skills"].keys():
            console.print(ikey + ": Tādas opcijas neeksistē", style="error")
            break

# while True:

def askQuestion(group, n):
    console.print(questions[group]["question"][n])
    questions["PHP"]["answered"][n] = input("Ievadiet atbildi => ")

askQuestion("PHP", "N1")

print(questions["PHP"]["answered"], questions["PHP"]["question"])

if questions["PHP"]["answers"]["N1"] == questions["PHP"]["answered"]["N1"]:
    console.print("[+] Atbilde ir pareiza: " + questions["PHP"]["answers"]["N1"], style="success")
    points += questions["PHP"]["points"]["N1"]
else:
    console.print("[-] Pareizā atbilde ir: " + questions["PHP"]["answers"]["N1"], style="error" )

console.print("Jūsu punktu skaits ir " + str(points), style="success")


# KOPSAVILKUMS

# table = Table(title="Kopsavilkums")

# table.add_column("Tēma", justify="left", style="cyan", no_wrap=True)
# table.add_column("Pareizā atbilde", style="magenta")
# table.add_column("punkti", justify="left", style="green")

# table.add_row(questions["PHP"]["question"]["N1"], questions["PHP"]["answers"]["N1"], points)
# table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")
# table.add_row("Dec 16, 2016", "Rogue One: A Star Wars Story", "$1,332,439,889")

# console = Console()
# console.print(table)