from cmath import nan
import pandas as pd 
import numpy as np
import re

file = (r'C:\Users\bryan\Desktop\Transactions\transactions.CSV')
refined = (r'C:\Users\bryan\Desktop\Transactions\refined.xlsx')
nf = pd.read_csv(file, parse_dates=['Date'])

citiCsv = (r'C:\Users\bryan\Desktop\Transactions\Citibank.CSV')

citi = pd.read_csv(citiCsv, parse_dates=['Date'])

nf['Month'] =pd.DatetimeIndex(nf['Date']).month
citi['Month'] = pd.DatetimeIndex(citi['Date']).month

print(nf.columns)

print(citi.columns)

df = pd.concat([nf,citi], axis=0, ignore_index=True)
print(df.fillna(0))


Citi = 'Status,Date,Description,Debit,Credit,Member Name'
NFed = "Date", "No.", "Description", "Debit", "Credit"


# print(df.groupby(['Month']).sum())
# print(df.loc[df['Description'] == 'Deposit - 0130EL12 TOTAL T'])
# print(df['Description'].unique())
print(df.loc[df['Description'].str.contains('Amzn.com')])
df.Description = df.Description.apply(lambda x: 'Amazon' if 'Amzn.com' in x else x)

# df['ChargeType'] = df['Description'].re.search(r'Amzn.com')
print(df['Description'].unique())
writer = pd.ExcelWriter(refined,engine='xlsxwriter')
df.to_excel(writer, sheet_name='refined')
writer.save()
