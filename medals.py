import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csvFile:
    headers = csvFile.readline().strip('\n').split(',')
    print(f'Column headers: {headers}')
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)
