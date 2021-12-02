import os
import time

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

