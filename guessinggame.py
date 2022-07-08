answer = 5

print("please guess a number between 1 and 10: ")

guess = int(input())

if guess != answer:
    if guess < answer:
        print("please guess higher")
    else: #guess must be higher than answer
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("well done")
    else:
        print("nope")
else: 
    print("you got it first time")
# old stuff
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you got it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done you got it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# else:
#     print("you got it first time")