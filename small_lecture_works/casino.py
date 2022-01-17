from random import randint

while True:
    input("Iegriezt ruleti")
    num1, num2, num3 = randint(1, 9), randint(1, 9), randint(1, 9)
    # num1, num2, num3 = 7,7,7
    if num1 == num2 and num2 == num3:
        print(f"Apsveicu, tu esi laimējis 100000000 Euro Cipari: {num1}{num2}{num3}")
        # break
    else:
        print(f"Diemžēl, jūs neko nevinējāt!    Cipari: {num1}{num2}{num3}")