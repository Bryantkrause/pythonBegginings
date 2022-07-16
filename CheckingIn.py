parrot = "norwegian blue"

letter = input("Enter a character: ")

if letter in parrot:
    print(f"{letter} is in {parrot}")
else:
    print("try again")