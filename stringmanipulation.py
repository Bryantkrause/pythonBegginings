parrot = "norway blue"

print(parrot[0:6:3])

Number = "9,123:321;456 789;456"

print(Number[1::4])

sepeparator = (Number[1::4])

print(sepeparator)

values = "".join(char if char not in sepeparator else " " for char in Number).split()
print([int(val) for val in values])
