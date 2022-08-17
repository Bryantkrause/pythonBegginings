import pandas as pd

file = 'stock_data.csv'
df = pd.read_csv(file, na_values={
    'revenue': [-1]
})
# print(df)

df.to_csv('new.csv', index=False, columns=['tickers', 'eps'])

file2 = 'stock_data.xlsx'

# for excel need converter function


def convert(cell):
    if cell == 'n.a.':
        return 'none'
    return cell


df2 = pd.read_excel(file2, converters={
    'people': convert
})

print(df2)

df2.to_excel('new.xlsx', sheet_name='stocks',
             startrow=1, startcol=2, index=False)
df_stocks = pd.DataFrame({
    'tickers': ['Google', 'WMT', 'MSFT'],
    'price': [845, 65, 64],
    'pe': [30.37, 14.26, 30.97],
    'eps': [27.82, 4.61, 2.12]
})

df_weather = pd.DataFrame({
    'day': ['1/1/2017', '1/2/2017', '1/3/2017'],
    'temperature': [32,35,28],
    'event': ['rain', 'sunny', 'snow']
})

with pd.ExcelWriter('stocks_weather.xlsx') as writer:
    df_stocks.to_excel(writer, sheet_name='stocks')
    df_weather.to_excel(writer, sheet_name='weather')


