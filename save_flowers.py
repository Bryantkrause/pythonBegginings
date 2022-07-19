data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

# plantsFile = "flowers_print.txt"

# with open(plantsFile, "w") as plants:
#     for plant in data:
#         print(plant, file=plants)

# newList = []

# with open(plantsFile) as plants:
#     for plant in plants:
#         newList.append(plant.rstrip())

# print(newList)

# plantsFile = "flowers_write.txt"

# with open(plantsFile, "w") as planter:
#     for plant in data:
#         planter.write(plant)

# print(data)
# string_rep = data.__str__()
# print(type(string_rep))

name = "test_number.txt"
with open(name, "w") as test:
    for i in range(10):
        print(i, file=test)

name = "test_number.txt"
with open(name, "w") as test:
    for i in range(10):
        test.write(str(i) + "\n")
