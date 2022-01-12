# infinite loop 
while True:
    try:
    # try code to errors
        # ask user to input actions
        firstNummber, operator, secondNummber = input("Enter an action. Example: 2 + 2 >> ").split()
        # convert to int type | from input default return a str
        firstNummber = int(firstNummber)
        secondNummber = int(secondNummber)
    except ValueError:
    # Try catch a ValueError Example: a + a
        print(">>> [error] incorrect value. ")
        continue
    except KeyboardInterrupt:
    # Try catch a KeyboardInterrupt Example: Ctrl + C
        print("\n\nBye, bye\n")
        exit()

    
    
    # checking operators and do action
    if operator == "+":
        print(firstNummber + secondNummber)
    elif operator == "-":
        print(firstNummber - secondNummber)
    elif operator == "*":
        print(firstNummber * secondNummber)
    elif operator == "/":
        print(firstNummber / secondNummber)
    elif operator == "%":
        print(firstNummber % secondNummber)
        
    # all code upper can be writen with one line under.
    # print(eval(input()))
