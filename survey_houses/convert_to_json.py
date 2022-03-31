import json
	
# Data to be written
dictionary = {
    "N1": """\n[option](1.)[/] Vai jūs esat ar mieru, ka mūsu māju kontrolēs gudrs AI - Altron ?\n""",
    "N2": """\n[option](2.)[/]  - Vai jūs apmierināti par saviem kainiņiem ? """,
    "N3": """\n[option](3.)[/]  - Vai vajag renovēt pagalma ielas ? """,
    "N4": """\n[option](4.)[/]  - Vai vajag aizliegt sētā iebraukt jebkurai mašīnai kuras logo nav TESLA ? """,
    "N5": """\n[option](5.)[/]  - Vai ierobežot laiku, kad bērni pagalmā var klausīties mūziku: Tikai 20:00 - 5:00 """,
    "N6": """\n[option](6.)[/]  - Vai vajag uzstādīt jaunu nodokli uz iebraukšanu pagalmā. Protams par visiem ienakumiem es nopirkšu jaunu TESLA, jo savādāk, kā es iebraukšu pagalmā. """
}
	
json_object = json.dumps(dictionary, indent = 4)

f = open("questions.json", "w")
f.write(json_object)
f.close()

print("Dati tika konvertēti")