from operator import truediv
import pandas as pd

df = pd.DataFrame({
    'date': ['5/1/2017', '5/2/2017', '5/3/2017', '5/1/2017', '5/2/2017', '5/3/2017', '5/1/2017', '5/2/2017', '5/3/2017' ],
    'city': ['ny', 'ny', 'ny', 'muble', 'muble', 'muble', 'bejin', 'bejin', 'bejin', ],
    'temp': [65,66,68,75,78,82,80,77,79],
    'humidity': [56,58,60,80,83,85,26,30,35]
})
# create file
# writer = df.to_csv('tutorialPivot.csv')

df.pivot(index='date',columns='city')
print(df.pivot(index='date',columns='city'))

print(df.pivot(index='date',columns='city',values='humidity'))

df2 = pd.DataFrame({
    'date': ['5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017', '5/1/2017', '5/1/2017', '5/2/2017', '5/2/2017'],
    'city': ['ny', 'ny', 'ny', 'ny', 'muble', 'muble', 'muble', 'muble', ],
    'temp': [65, 66, 68, 75, 78, 82, 80, 77],
    'humidity': [56, 58, 60, 80, 83, 85, 26, 30]
})

print(df2)
# mean is default
print(df2.pivot_table(index='city',columns='date', aggfunc='sum', margins=True))
print(df2.pivot_table(index='city',columns='date', margins=True))

df3 = pd.DataFrame({
    'date': ['5/1/2017', '5/2/2017', '5/3/2017', '12/1/2017', '12/2/2017', '12/3/2017'],
    'city': ['ny', 'ny', 'ny', 'ny', 'ny', 'ny'],
    'temp': [65, 66, 68, 75, 78, 82],
    'humidity': [56, 58, 60, 80, 83, 85]
})
df3['date'] = pd.to_datetime(df3['date'])
print(type(df3['date'][0]))
print(df3.pivot_table(index=pd.Grouper(
    freq='M', key='date'), columns='city', aggfunc='sum'))

