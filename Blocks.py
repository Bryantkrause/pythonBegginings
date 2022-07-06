start = 1

end = 100



for i in range(1, 2):
    print(f"No. {i:2} squared is {i ** 2:3} and cubed is {i ** 3:4}")
    print("*" * 80)

for i in range(start, end):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")