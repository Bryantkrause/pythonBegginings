answer = 5

print("please guess a number between 1 and 10: ")

guess = int(input())

if guess == answer:
    print("you got it")
else: 
    if guess < answer:
        print("please guess higher")
    else: #guess must be higher than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done")
    else:
        print("nope that is too bad")
