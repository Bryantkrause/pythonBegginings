import csv

cerealsFile = 'country_info.txt'

with open(cerealsFile, encoding='utf-8', newline='') as csvFile:
    reader = csv.DictReader(csvFile)
    for row in reader:
        print(row)
