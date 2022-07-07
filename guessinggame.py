answer = 5

print("please guess a number between 1 and 10: ")

guess = int(input())

if guess < answer:
    print("Please guess higher")
elif guess > answer:
    print("Please guess lower")
else:
    print("you got it first time")