import pandas as pd

file = 'stock_data.csv'
df = pd.read_csv(file, na_values={
    'revenue': [-1]
})
print(df)
