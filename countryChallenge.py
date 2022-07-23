from locale import currency
import csv

codeLookUp = []
fileName = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'

countries = {}
with open(fileName, encoding='utf-8', newline='') as countryFile:
    # get headings
    headings = countryFile.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(headings):
        headings[index] = heading.casefold()

    dictReader = csv.DictReader(countryFile, dialect=dialect, fieldnames=headings)
    for row in dictReader:
        # countries[country.casefold()] = country_dict
      
        countries[row['country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['cc'].casefold()] = row
# print(countries)
while True:
    chosen = input('please enter country:')
    countryKey = chosen.casefold()
    if countryKey in countries:
        country_data = countries[countryKey]
        print(f"The capital of {chosen} is {country_data['capital']}")
    elif chosen == 'quit':
        break
