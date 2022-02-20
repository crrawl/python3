try:
    age = int(input("Please Enter Your Age: "))

except ValueError:
    print("ValueError: Jums jaievada skaitlis.")
    exit()
except KeyboardInterrupt:
    print("\nTiksimies nākamreiz :(")
    exit()

if __name__ == "__main__":
    if age >= 18:
        print(">>> You are eligible to vote")
    else:
        print(">>> You are NOT eligible to vote")
