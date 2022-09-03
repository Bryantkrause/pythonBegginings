from cmath import nan
import pandas as pd 
import numpy as np

file = (r'C:\Users\bryan\Desktop\Transactions\transactions.CSV')

nf = pd.read_csv(file, parse_dates=['Date'])

citiCsv = (r'C:\Users\bryan\Desktop\Transactions\Citibank.CSV')

citi = pd.read_csv(citiCsv, parse_dates=['Date'])

nf['Month'] =pd.DatetimeIndex(nf['Date']).month
citi['Month'] = pd.DatetimeIndex(citi['Date']).month

print(nf.columns)

print(citi.columns)

df = pd.concat([nf,citi], axis=0, ignore_index=True)
print(df.fillna(0))




# print(df)

print(df.groupby(['Month']).sum())
print(df.loc[df['Description'] == 'Deposit - 0130EL12 TOTAL T'])
print(df['Description'].unique())
Citi = 'Status,Date,Description,Debit,Credit,Member Name'

NFed = "Date","No.","Description","Debit","Credit"