from locale import currency

codeLookUp =[]
fileName = 'country_info.txt'

countries = {}
with open(fileName) as countryFile:
    countryFile.readline()
    for row in countryFile:
        data = row.strip('\n').split('|')
        country, capital, code, code3, dialing, timezone, currency = data
        # print(country, capital, code, code3, dialing, timezone, currency, sep='\n\t')
        country_dict = {
            'name': country,
            'capital': capital,
            'country_code': code,
            'cc3': code3,
            'dialing_code': dialing,
            'timezone': timezone,
            'currency': currency
        }
        # print(country_dict)
        countries[country.casefold()] = country_dict
        # codeLookUp[code.casefold()] = country
        countries[code.casefold()] = country_dict
# print(countries)
while True:
    chosen = input('please enter country:')
    countryKey= chosen.casefold()
    if countryKey in countries:
        country_data = countries[countryKey]
        print(f"The capital of {chosen} is {country_data['capital']}")
    elif chosen == 'quit':
        break
