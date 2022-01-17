import random

while True:
    a = random.randint(1, 10)
    b = int(input("Ievadi skaitli="))
    if a == b:
        print("Uzminēji")
        print(str(int(a)))
        break
    else:
        print("Mini vēl")
        print(str(a))
