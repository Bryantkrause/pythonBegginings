import pandas

df = pandas.read_csv(
    r"C:\Users\bkrause\Documents\CodeMe\Rebirth\pythonBeginings\statsAndJunk\thing2.csv")


d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)

print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

X = df[features]
y = df['Go']

print(X)
print(y)
