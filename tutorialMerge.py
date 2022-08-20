import pandas as pd

df1 = pd.DataFrame({
    'temp': [50, 5, 12, 69],
    'city': ['ny', 'chicago', 'orlando', 'baltimore']
})
df2 = pd.DataFrame({
    'humidity': [25, 35, 45, 55],
    'city': ['chicago', 'orlando', 'ny', 'sf']
})
# how = type of join on = join placement
df3 = pd.merge(df1, df2, on='city', how='outer', indicator=True)

print(df3)

df4 = pd.DataFrame({
    'humidity': [69, 96, 69, 96],
    'city': ['chicago', 'orlando', 'ny', 'sf']
})
df5 = pd.DataFrame({
    'humidity': [25, 35, 45, 55],
    'city': ['chicago', 'orlando', 'ny', 'sf']
})

df6 = pd.merge(df4,df5, on='city',suffixes=('_left','_right'))
print(df6)