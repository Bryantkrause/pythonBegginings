import pandas as pd
# df = pd.read_csv('weather_data.csv')



weather_data = {
    'day': ['1/1/2017', '1/2/2017', '1/3/2017', '1/4/2017', '1/5/2017', '1/6/2017'],
    'temperature': [32, 35, 28, 24, 32, 31],
    'windspeed': [6, 7, 2, 7, 4, 2],
    'event': ['rain', 'sunny', 'snow', 'snow', 'rain', 'sunny']
}
df = pd.DataFrame(weather_data)
# print(df.shape)
rows, columns = df.shape
# print(rows, columns)

# print(df.head(2))
# print(df.tail(2))

# print(df[2:5])

# print(df.columns)

# print(df.event)

# print(type(df['event']))

# print(df[['event','day']])

# print(df['temperature'].max())
# print(df.describe())

print(df.temperature>=32)
print(df[df.temperature>=32])
print(df[df.temperature==df.temperature.max()])
print(df[['day','temperature']][df.temperature==df.temperature.max()])

print(df.index)
# this sets index
df.set_index('day', inplace=True)

print(df.loc['1/3/2017'])

df.reset_index(inplace=True)

print(df)