import difflib
from textwrap import fill
import pandas as pd

file = 'temp2missing.csv'
df = pd.read_csv(file, parse_dates=['day'])
df.set_index('day', inplace=True)

# replaces all missing with same value
filler = df.fillna(0)

print(filler)

# this method supplies values directly
changeV = df.fillna({
    'temperature': 0,
    'windspeed': 0,
    'event': 'no event'
})
print(changeV)

# this method carries forward data from previous row
methoderff = df.fillna(method='ffill')
print(methoderff)

# this method carries backward data from row below
methodbf = df.fillna(method='bfill')
print(methodbf)

# set row limit of filling blank data
methodL = df.fillna(method='ffill', limit=1)
print(methodL)

# by default is linear but comes with many many many methods
dfI = df.interpolate()
print(dfI)
# time method example
dfIt = df.interpolate(method='time')
print(dfIt)

# remove all rows with any missing data
dfdrop = df.dropna()
print(dfdrop)

# only drop if all row missing
dfdropAll = df.dropna(how='all')
print(dfdropAll)

# insert mising data
dt= pd.date_range('01-01-2017', '01-11-2017')
idx = pd.DatetimeIndex(dt)
dater =df.reindex(idx)
print(dater)

newInter = dater.interpolate(method='time')
print(newInter)
