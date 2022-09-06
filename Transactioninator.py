from cmath import nan
from msilib.schema import Condition
from pickle import FALSE
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



df = pd.concat([nf,citi], axis=0, ignore_index=True)
print(df.fillna(0))

conditions = [
    df['Description'].str.contains(r'Charter Service', na=False),
    df['Description'].str.contains(r'CITI AUTOPAY', na=False),
    df['Description'].str.contains(r'CITI CARD', na=False),
    df['Description'].str.contains(r'HOMESITE INS PREM', na=False),
    df['Description'].str.contains(r'HPS MHC', na=False),
    df['Description'].str.contains(r'MediCalforFamily', na=False),
    df['Description'].str.contains(r'NINTENDO', na=False),
    df['Description'].str.contains(r'PAYPAL', na=False),
    df['Description'].str.contains(r'SO CAL EDISON', na=False),
    df['Description'].str.contains(r'SPECTRUM', na=False),
    df['Description'].str.contains(r'T-MOBILE', na=False),
    df['Description'].str.contains(r'UNITED FIN CAS INS', na=False),
    df['Description'].str.contains(r'ARCO', na=False),
    df['Description'].str.contains(r'CARLS JR', na=False),
    df['Description'].str.contains(r'CHEESECAKE', na=False),
    df['Description'].str.contains(r'CHICK-FIL-A', na=False),
    df['Description'].str.contains(r'CHIPOTLE', na=False),
    df['Description'].str.contains(r'COFFEE BEAN', na=False),
    df['Description'].str.contains(r'COSTCO', na=False),
    df['Description'].str.contains(r'0130EL12 TOTAL T', na=False),
    df['Description'].str.contains(r'DOMINO', na=False),
    df['Description'].str.contains(r'Etsy', na=False),
    df['Description'].str.contains(r'GoFundMe', na=False),
    df['Description'].str.contains(r'CAR WASH', na=False),
    df['Description'].str.contains(r'HABIT', na=False),
    df['Description'].str.contains(r'IN N OUT', na=False),
    df['Description'].str.contains(r'JOE SCHMOE', na=False),
    df['Description'].str.contains(r'Kindle', na=False),
    df['Description'].str.contains(r'LITTLE LADYBUG', na=False),
    df['Description'].str.contains(r'MCDONALD', na=False),
    df['Description'].str.contains(r'NEW BALANCE', na=False),
    df['Description'].str.contains(r'AUTO PARTS', na=False),
    df['Description'].str.contains(r'PANDA EXPRESS', na=False),
    df['Description'].str.contains(r'PIEOLOGY', na=False),
    df['Description'].str.contains(r'PIZZA HUT', na=False),
    df['Description'].str.contains(r'Amzn', na=False),
    df['Description'].str.contains(r'APPLECOM', na=False),
    df['Description'].str.contains(r'CSC SERVICEWORKS', na=False),
    df['Description'].str.contains(r'GOOGLE', na=False),
    df['Description'].str.contains(r'HEALTHCARE', na=False)
    ]

choices = [
    'Charter Service', 'CITI AUTOPAY', 'CITI CARD', 'HOMESITE INS PREM', 'HPS MHC', 'MediCalforFamily',
    'NINTENDO', 'PAYPAL', 'SO CAL EDISON', 'SPECTRUM', 'T-MOBILE', 'UNITED FIN CAS INS', 'ARCO', 'CARLS JR',
    'CHEESECAKE', 'CHICK-FIL-A', 'CHIPOTLE', 'COFFEE BEAN', 'COSTCO', 'Pay Check', 'DOMINOS',
    'Etsy', 'GoFundMe', 'CAR WASH', 'HABIT', 'IN N OUT', 'JOE SCHMOE', 'Kindle', 'LITTLE LADYBUG',
    'MCDONALDS', 'SHOES', 'AUTO PARTS', 'PANDA EXPRESS', 'PIEOLOGY', 'PIZZA HUT', 'AMAZON', 'APPLECOM',
    'CSC SERVICEWORKS', 'GOOGLE', 'HEALTHCARE'
]
print(len(conditions))
print(len(choices))

df['ChargeType'] = np.select(conditions, choices, default='NA')
# Citi = 'Status,Date,Description,Debit,Credit,Member Name'
# NFed = "Date", "No.", "Description", "Debit", "Credit"


# print(df.groupby(['Month']).sum())
# print(df.loc[df['Description'] == 'Deposit - 0130EL12 TOTAL T'])
# print(df['Description'].unique())
# print(df.loc[df['Description'].str.contains('Amzn.com')])
# df.Description = df.Description.apply(lambda x: 'Amazon' if 'Amzn.com' in x else x)

# df['ChargeType'] = df['Description'].re.search(r'Amzn.com')
# print(df['Description'].unique())
writer = pd.ExcelWriter(refined,engine='xlsxwriter')
df.to_excel(writer, sheet_name='refined')
writer.save()
