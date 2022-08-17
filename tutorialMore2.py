import pandas as pd

csv = 'weather_data.csv'
df =  pd.read_csv(csv)
excel = 'weather_data.xlsx'
sheet = 'weather_data'
dfE = pd.read_excel(excel, sheet)
print(df)
print(dfE)
weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['rain', 'sunny', 'snow', 'snow', 'rain', 'sunny']
}
dfD = pd.DataFrame(weather_data)

print(dfD)