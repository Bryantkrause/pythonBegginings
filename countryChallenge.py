from locale import currency
import csv

codeLookUp = []
fileName = 'country_info.txt'

countries = {}
with open(fileName, encoding='utf-8', newline='') as countryFile:
    dictReader = csv.DictReader(countryFile, delimiter='|')
    for row in dictReader:
        # countries[country.casefold()] = country_dict
      
        countries[row['Country'].casefold()] = row
        # countries[code.casefold()] = country_dict
        countries[row['CC'].casefold()] = row
# print(countries)
while True:
    chosen = input('please enter country:')
    countryKey = chosen.casefold()
    if countryKey in countries:
        country_data = countries[countryKey]
        print(f"The capital of {chosen} is {country_data['Capital']}")
    elif chosen == 'quit':
        break
