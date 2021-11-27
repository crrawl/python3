import os

''' 
Pārbauda, kāda operētājsistēma ir lietotājam
skatoties no rezultāta izvadas attiecīga komanda
'''

if os.name == "nt": # posx, java, nt
    os.system("cls")
else:
    os.system("clear")

# Pziņo, kā iziet no cikla
print(">> Iziet no programmas var ar kombināciju (Ctrl + C)")

# Liek atkārtoties kodam bezgalīgi
while True:
    # Prasa ciparu. Sagaida, ka ievadīs: type int
    number = int(input("Ievadiet pozitīvu divciparu skaitli -> "))
    
    # Pārveidoju number uz string, lai varētu noteikt tās garumu.
    
    numb = str(number)
    # Iegūst simbolu skaitu iekš mainīgā number
    num = len(numb)

    # Pārbauda vai ir mainīgajā ir 2 simboli
    if num != 2:
        print("Ir jāievada divciparu skaitlis")
    else:
        print(f"Jūs ievadijāt {number}")

        ''' Izveido mainīgo int d(digit).
            Katrā iterācijā d == number[d+1] tad
            to konverto uz list'''
        result = [int(d) for d in str(number)]
        
        # Summē 2 ievadītos skaitļus un izvada 
        print(result[0] + result[1])
