
from random import randint


print("""
Sveicināts iekš spēles "GHOST"
sakrāj pēc iespējas vairāk punktus :)
Lai izietu no spēles ievadi kombināciju
(Ctrl + C)
""")

points = 0
try:
    while True:

        rand_door = randint(1,3)
        print("""
Tev priekšā ir trīs durvis…
Aiz vienām ir spoks.
Kuras durvis tu atvērsi?""")
        # print(rand_door) # > debug
        door = int(input("1,2 vai 3? "))

        if door != int(rand_door):
            print("Spoka nav!")
            points += 1
        elif door == int(rand_door):
            print(f"""
Spoks!
Bēdz prom!

Spēle beigusies. Tu ieguvi spēle {points} punktus.
            """)
            points = 0
        else:
            print("""
    Tādas durvis neeksistē!
            """)



        input("ENTER lai turpinātu")
except KeyboardInterrupt:
    print(f"\nTiksimies citreiz: Jūsu punktu skaits {points}")

"""
if record > points:
    record = points
    print(f"Jūsu rekords ir {record}")
"""
