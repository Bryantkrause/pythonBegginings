for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # this use of format reserves that number of columns for space so a {0:2} reservers 2 columns

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(
        i, i ** 2, i ** 3
        )) # use <> operators to choose alingment type 

print("Pi is aprox {0:12}".format(22/7))
print("Pi is aprox {0:12f}".format(22/7))
print("Pi is aprox {0:12.50f}".format(22/7))
print("Pi is aprox {0:52.50f}".format(22/7))
print("Pi is aprox {0:62.50f}".format(22/7))
print("Pi is aprox {0:72.50f}".format(22/7))
