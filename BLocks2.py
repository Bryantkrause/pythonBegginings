name = input("Please enter your name: ")
age = int(input(f"How old are you, {name}? "))
print(age)

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print(f"Please come back in {18 - age} years.")

if age < 18:
    print(f"Please come back in {18 - age} years.")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")