

# while True:
#     x = int(input("Please enter an integer: "))
#     if x < 0:
#         print("X is negative")
#     elif x == 0:
#         print("X is null")
#     else:
#         print("X is positive")
# grade = "Unknown"
# score = int(input("Enter a points"))

# if score >= 90: 
#     grade = "A"
# else:
#     if score >= 80: 
#         grade = "B"
#     else:
#         if score >= 70: 
#             grade = "C"
#         else:
#             grade = "F"
# print(grade)

# country = input("Enter a country ").lower()
# if country == "japan" or country == "nihon":
#     print("Capital city of japan is Tokiyo")
# elif country == "latvia" or country == "latvija":
#     print("Capital city of Latvia is Riga")
# elif country == "russian":
#     print("Capital city of Russian is Moscow")
# else:
#     print("You entered country who i don't known.")


# age = int(input("What is your age? "))
# if age > 70:
#     print("You need to test your eyesight")
# elif age > 16:
#     print("You can drive")
# else:
#     print("You cannot drive")

# age = int(input("Enter your age"))
# if age >= 18:
#     print("Adult")
# elif age >= 13:
#     print("Teenager")
# else:
#     print("Child")
    
# answer = input("What is your favourite room at the house ")
# if answer == "kitchen":
#     print("You love food")
# elif answer == "bedroom":
#     print("You love sleep")
# elif answer == "school":
#     print("You love be smart :)")

# print("""First we need to know you. 
# Eneter your name please.""")

# name = input("Name: ")
# print(f"Welcome, {name} !")

# criminal = input("Are you a criminal? (y/n): ").lower()
# if criminal == "y":
#     print("Just, bad boy")
# elif criminal == "n":
#     print("Jesus kid")

# num = int(input("Ener any nummber: "))
# flag = num % 2

# if flag == 0:
#     print("             ")
# elif flag == 1:
#     print("         ")
# else:
#     print("     ")

 
# 1 point
# Kas tiks izvadīts uz ekrāna?
while True:

    is_snowing = input("Is snowing ?").lower()
    
    if is_snowing == "yes":
        print("wear snackers")
    elif is_snowing == "no":
        print("wear boots")
    else: print("Unknown answer")