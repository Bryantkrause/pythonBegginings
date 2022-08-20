import pandas as pd

file = 'tutgroupby.xlsx'
df = pd.read_excel(file)
print(df)
gb = df.groupby('city')
for city, city_df in gb:
    print(city)
    print(city_df)

print(gb.get_group('paris'))

print(gb.max())
print(gb.mean())
print(gb.describe())


