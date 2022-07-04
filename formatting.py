for i in range(1, 13):
    # this use of format reserves that number of columns for space so a {0:2} reservers 2 columns
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(
        i, i ** 2, i ** 3))

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(
        i, i ** 2, i ** 3
    ))  # use <> operators to choose alingment type

print("Pi is aprox {0:12}".format(22/7))
print("Pi is aprox {0:12f}".format(22/7))
print("Pi is aprox {0:12.50f}".format(22/7))
print("Pi is aprox {0:52.50f}".format(22/7))
print("Pi is aprox {0:62.50f}".format(22/7))
pi = 22/7
print("Pi is aprox {0:72.50f}".format(22/7))
print(f"Pi is aprox {pi:12.50f}")
# who needs .format when you can just f it

meal2 = "spam\neggs\nbeans"
meal1 = """spam
eggs
beans"""

print(meal2)
print(meal1)

a = 45
b = 15
c = 3

print(a - b / c)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])
