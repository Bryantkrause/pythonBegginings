import pandas as pd

file = 'tutorialTimeSeries.csv'

df = pd.read_csv(file, parse_dates=['Date'], index_col='Date')
print(df.head())

print(type(df.index))

print(df.index)

print(df['2017-01'].Close.mean())

print(df['2017-01':'2017-02'])

print(df.Close.resample('M').mean())
