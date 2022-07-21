import csv

file = 'cereal_grains.csv'

with open(file, encoding='utf-8', newline='') as csvFile:
    # print(csvFile)
    reader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
