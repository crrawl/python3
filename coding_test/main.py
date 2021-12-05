# from logging import error
import os
import sys
import time
import json
import random


from rich import emoji
from rich.progress import track
from rich.console import Console
from rich.theme import Theme
from rich.table import Table


# FUNCTIONS 

def askQuestion(group, n):
    global  points, correct, incorrect
    # Ask question 
    print("---------------------------------------")
    console.print(questions[group]["question"][n])
    print("---------------------------------------")

    questions[group]["answered"][n] = input("Ievadiet atbildi => ").lower()
    # Check a answer
    if questions[group]["answers"][n] == questions[group]["answered"][n]:
        print("")
        console.print("[+] Atbilde ir pareiza: " + questions[group]["answers"][n], style="success")
        print("")
        points += questions[group]["points"][n]
        correct += 1
    else:
        print("")
        console.print("[-] Pareizā atbilde ir: " + questions[group]["answers"][n], style="error" )
        print("")
        incorrect += 1

def getRandQuestNumList():
    list = []
    n = 1
    while n < 50:
        n += 1 
        rand = random.randint(1, 10)
        r = "N" + str(rand)

        if r not in list: 
            list.append(r)
        if len(list) == 10:
            break
    return list

def getSkillItem():
    skills = random.choice(PSkills)
    skill = questions["skills"][skills]
    return skill 

def giveQuestion():
    list = getRandQuestNumList()

    for key in list:
        skill = getSkillItem()
        askQuestion(skill, key)

# Color Theme: create new colour theme
custom_theme = Theme({  "error" : "bold red", 
                        "success" : "bold green", 
                        "attention" : "bold yellow", 
                        "warning" : "bold magenta",
                        "option" : "#4169E1",
                        "blocked": "#383B40"
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

# Veriables

# points
points = 0

# corret / incorrect answers
correct = 0
incorrect = 0

# emojis
global emojies
emojies = ["😒", "😢", "😭", "😟", "😞", "😥", "😖", "☹", "😔"]

# Import json dictiionary
with open('dictionary.json') as dict:
    questions = json.load(dict)


# Sey to user, how to quit from app
console.print(">> Iziet no programmas var ar kombināciju (Ctrl + C)", style="bold white")

# introduction
console.print(questions["start"]["WELCOME"])
try:
    # Turn eneter to continiune
    input()  

    while True:

        # requiring a name
        current_username = str(input("Ievadiet savu vārdu => "))

        if current_username == "" or len(current_username) < 4 or len(current_username) > 24:
            console.print("[error][-][/] Jums jāievada korekts vārds")
            continue

        # requiring user to enter skills
        console.print(questions["start"]["question"]["N1"])

        # Enter a skills key then split on "," char 
        PSkills = str(input("Atbildi ievadiet ar ','. Piemērs a,e => ")).replace(" ","").lower().split(",")
        if len(PSkills) < 0:
            console.print("[error][-][/] Jums jāizvēlas vismaz viena valoda")

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

        try:
            giveQuestion()
            show_table = True

        except KeyError:
            for key in PSkills:
                if key not in questions["skills"].keys():
                    console.print("[error][-][/] Jums jāizvēlas viens no pieejamajiem atbilžu variantiem.")
                    show_table = False
                    break



        # KOPSAVILKUMS
            
        if show_table:
            def step(step):
                print(step)
                
            for step in track(range(100)):
                
                console.print("Jūsu punktu skaits ir " + str(points), style="success")
                table = Table(title="Kopsavilkums")

                table.add_column("Vārds", style="magenta")
                table.add_column("Pareizās atbildes", style="green")
                table.add_column("Nepareizās atbildes", justify="left", style="magenta")
                table.add_column("punkti", justify="left", style="green")

                table.add_row(str(current_username), str(correct), str(incorrect), str(points))
                
                console = Console()
                console.print(table)

            if points <= 3 and len(PSkills) == 1:
                console.print("\n[RESULT][!] [white]Tev vajadzētu pamēģināt izvēlēties vieglāku valodu.[/]\n", style="green")
            elif points >= 4 and points <= 6 and len(PSkills) == 1:
                console.print("\n[RESULT][!] [white]Nešaubīšos ja tu vēl deletants programmēšanas sfērā, kurš vēl nav uzspējis vilties savos sapņos[/]\n", style="green")
            elif points >= 7 and points <= 10 and len(PSkills) == 1:
                console.print("\n[RESULT][!] [white]Zini kurā valodā esi spēcīgs/-a un pierādiji, ka ne tikai proti smuki runāt, bet arī ar darbiem pierādīt[/]\n", style="attention\n")
            elif points >= 1 and points <= 3 and len(PSkills) == 2:
                console.print("\n[RESULT][!] [white]Liecies pārliecināts savās zināšanās, bet kaut kas vēl trūkst[/]\n", style="green")
            elif points >= 4 and points <= 6 and len(PSkills) == 2:
                console.print("\n[RESULT][!] [white]Esi pārliecināts savās zināšanās un saproti ko dari, bet vēl vajag pamācīties[/]\n", style="green")
            elif points >= 7 and points <= 10 and len(PSkills) == 2:
                console.print("\n[RESULT][!] [white]Esi pārliecināts savās zināšanās un tiešām saproti ko dari[/]\n", style="green")
            elif points >= 1 and points <= 3 and len(PSkills) == 3:
                console.print("\n[RESULT][!] [white]Pamēģināji uzreiz grūtāko variantu, jo domāji es, kā autors esmu ne ļoti gudrs un grūtus jautājumus neuzdošu[/]\n", style="green")
            elif points >= 4 and points <= 6 and len(PSkills) == 3:
                console.print("\n[RESULT][!] [white]Mēģināji uzreiz visas trīs valodas, bet tomērt tev vajadzētu vēl pamācīties.[/]\n", style="green")
            elif points >= 7 and points <= 10 and len(PSkills) == 3:
                console.print("\n[RESULT][!] [white]Noteikti ir pieredze un saproti, ko nozīmē būt programmistam. Skaties uz deletantiem no augšas uz leju.\n Tajā sakitā uz mani, jo tev liekas šie jautajumi pārāk viegli un tizli. Un vispār priekš bērnudārzniekiem taisīts tests[/]\n", style="green")
            elif points == 0:
                console.print("\n[RESULT][!] [white] Tu esi anskills, iemācies lietot Google vismaz[/]\n", style="green")
       
        break
except KeyboardInterrupt:
    
    emoji = random.choice(emojies)

    console.print("\n[attention]Ceru palaidīsi mani vēlreiz [/]" + emoji)
    sys.exit()
