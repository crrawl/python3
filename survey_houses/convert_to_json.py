import json
	
# Data to be written
dictionary ={
    "N1": """\n[option](1.)[/] Vai jūs esat ar mieru, ka mūsu māju kontrolēs gudrs AI - Altron ?
[white]-[/] [error](Nē)[/], [white]/[/] [warning](Patreiz neitrāls)[/], [white]+[/] [success]Jā![/], \n""",
    "N2": """\n[option](2.)[/]  - SUKKAAA ?
[white]-[/] [error](Nē)[/], [white]/[/] [warning](Patreiz neitrāls)[/], [white]+[/] [success]Jā![/], \n""",
    "N3": """\n[option](3.)[/]  - SUKKAAA 3333333 ?
[white]-[/] [error](Nē)[/], [white]/[/] [warning](Patreiz neitrāls)[/], [white]+[/] [success]Jā![/], \n"""
}
	
json_object = json.dumps(dictionary, indent = 4)

f = open("questions.json", "w")
f.write(json_object)
f.close()

print("Dati tika konvertēti")