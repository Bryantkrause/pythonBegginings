import csv

file = 'country_info.txt'

with open(file, encoding='utf-8', newline='') as csvFile:
    # print(csvFile)
    sample = ""
    for line in range(3):
        sample += csvFile.readline()
    dialectC = csv.Sniffer().sniff(sample)
    dialectC.skipinitialspace = True
    csvFile.seek(0)
    # reader = csv.reader(csvFile, delimiter='|')
    reader = csv.reader(csvFile, dialect=dialectC)
    for row in reader:
        print(row)

print('break break break')
# below code uses sniffer to identify the below information
attributes = [
    'delimiter',
    'doublequote',
    'escapechar',
    'lineterminator',
    'quotechar',
    'quoting',
    'skipinitialspace']
for attribute in attributes:
    print(f'{attribute}: {repr(getattr(dialectC, attribute))}')
