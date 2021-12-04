from logging import error
import os
import sys
import time
import json
import random
from rich import emoji


from rich.console import Console
from rich.theme import Theme
from rich.table import Table


try:
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

    # Turn eneter to continiune
    input()  
    skip = 'y'
    while skip == 'y':
        # requiring a name
        current_username = str(input("Ievadiet savu vārdu => "))
        if current_username == "" or len(current_username) < 4:
            console.print("[error][-][/] Jums jāievada korekts vārds")
            continue

        # requiring user to enter skills
        console.print(questions["start"]["question"]["N1"])

        # Enter a skills key then split on "," char 
        PSkills = str(input("Atbildi ievadiet ar ','. Piemērs a,e => ")).replace(" ","").lower().split(",")

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

        def giveQuestion():
            list = getRandQuestNumList()

            for key in list:
                skill = getSkillItem()
                askQuestion(skill, key)



        giveQuestion()

        console.print("Jūsu punktu skaits ir " + str(points), style="success")


        # KOPSAVILKUMS

        table = Table(title="Kopsavilkums")
        table.add_column("Vārds", style="magenta")
        table.add_column("Pareizās atbildes", style="magenta")
        table.add_column("Nepareizās atbildes", justify="left", style="green")
        table.add_column("punkti", justify="left", style="green")

        table.add_row(str(current_username) ,str(correct), str(incorrect), str(points))

        console = Console()
        console.print(table)
        skip = str(input("[success]'y'[/] lai turpinātu, [error]'ENTER'[/] lai beigtu "))

except KeyboardInterrupt:
    
    emoji = random.choice(emojies)
        
    console.print("\n[attention]Ceru palaidīsi mani vēlreiz [/]" + emoji)
    sys.exit()