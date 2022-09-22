from cmath import nan
from msilib.schema import Condition, Directory
from pickle import FALSE
import pandas as pd
import numpy as np
import re
import os
from pathlib import Path


file = (r'C:\Users\bryan\Desktop\Transactions\transactions.CSV')
refined = (r'C:\Users\bryan\Desktop\Transactions\refined.xlsx')
directory = Path(
    'C:/Users/bryan/Desktop/Transactions/refined.xlsx')
nf = pd.read_csv(file, parse_dates=['Date'])

citiCsv = (r'C:\Users\bryan\Desktop\Transactions\Citibank.CSV')

citi = pd.read_csv(citiCsv, parse_dates=['Date'])

nf['Month'] = pd.DatetimeIndex(nf['Date']).month
citi['Month'] = pd.DatetimeIndex(citi['Date']).month
nf['Location'] = 'Navy Fed'
citi['Location'] = 'CitiBank'


df = pd.concat([nf, citi], axis=0, ignore_index=True)
print(df.fillna(0))
df = df.fillna(0)
df['Total'] = df['Debit'] + df['Credit']
# df['Description'] = df['Description'].str.upper()
df['Description'] = df['Description'].apply(lambda x: x.upper())
conditions = [
    df['Description'].str.contains(r'CHARTER SERVICE', na=False),
    df['Description'].str.contains(r'CITI AUTOPAY', na=False),
    df['Description'].str.contains(r'CITI CARD', na=False),
    df['Description'].str.contains(r'HOMESITE INS PREM', na=False),
    df['Description'].str.contains(r'HPS MHC', na=False),
    df['Description'].str.contains(r'MEDICALFORFAMILY', na=False),
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
    df['Description'].str.contains(r'ETSY', na=False),
    df['Description'].str.contains(r'GOFUNDME', na=False),
    df['Description'].str.contains(r'CAR WASH', na=False),
    df['Description'].str.contains(r'HABIT', na=False),
    df['Description'].str.contains(r'IN N OUT', na=False),
    df['Description'].str.contains(r'JOE SCHMOE', na=False),
    df['Description'].str.contains(r'KINDLE', na=False),
    df['Description'].str.contains(r'LITTLE LADYBUG', na=False),
    df['Description'].str.contains(r'MCDONALD', na=False),
    df['Description'].str.contains(r'NEW BALANCE', na=False),
    df['Description'].str.contains(r'AUTO PARTS', na=False),
    df['Description'].str.contains(r'PANDA EXPRESS', na=False),
    df['Description'].str.contains(r'PIEOLOGY', na=False),
    df['Description'].str.contains(r'PIZZA HUT', na=False),
    df['Description'].str.contains(r'AMZN', na=False),
    df['Description'].str.contains(r'APPLECOM', na=False),
    df['Description'].str.contains(r'CSC', na=False),
    df['Description'].str.contains(r'GOOGLE', na=False),
    df['Description'].str.contains(r'HEALTHCARE', na=False),
    df['Description'].str.contains(r'TARGET', na=False),
    df['Description'].str.contains(r'TO SHARES', na=False),
    df['Description'].str.contains(r'FROM SHARES', na=False),
    df['Description'].str.contains(r'STATER', na=False),
    df['Description'].str.contains(r'STEAM', na=False),
    df['Description'].str.contains(r'WALMART', na=False),
    df['Description'].str.contains(r'DIVIDEND', na=False),
    df['Description'].str.contains(r'TACO BELL', na=False),
    df['Description'].str.contains(r'RUBIOS', na=False),
    df['Description'].str.contains(r'WINGSTOP', na=False),
    df['Description'].str.contains(r'SCANMOBILE', na=False),
    df['Description'].str.contains(r'ZENNI OPTICAL', na=False),
    df['Description'].str.contains(r'STARBUCKS', na=False),
    df['Description'].str.contains(r'SIMPLE GREEK', na=False),
    df['Description'].str.contains(r'HOME DEPOT', na=False),
    df['Description'].str.contains(r'ROUND TABLE', na=False),
    df['Description'].str.contains(r'VOLCANO BURGER', na=False),
    df['Description'].str.contains(r'TRINITY EUROPEAN', na=False),
    df['Description'].str.contains(r'PAID CHECK', na=False),
    df['Description'].str.contains(r'RUNNERS HIGH', na=False),
    df['Description'].str.contains(r'FISH IN A BOTTLE', na=False),
    df['Description'].str.contains(r'YOGURT', na=False),
    df['Description'].str.contains(r'AUTOPAY AUTO-PMT', na=False),
    df['Description'].str.contains(r'ZELLEAUTOMATED', na=False),
    df['Description'].str.contains(r'EL POLLO LOCO', na=False),
    df['Description'].str.contains(r'ONLINE PAYMENT, THANK YOU', na=False)
]

choices = [
    'CHARTER SERVICE', 'CITI AUTOPAY', 'CITI CARD', 'RENTERS INSURANCE', 'HPS MHC', 'MEDICAL',
    'NINTENDO', 'PAYPAL', 'SO CAL EDISON', 'SPECTRUM', 'T-MOBILE', 'CAR INSURANCE', 'ARCO', 'CARLS JR',
    'CHEESECAKE', 'CHICK-FIL-A', 'CHIPOTLE', 'COFFEE BEAN', 'COSTCO', 'Pay Check', 'DOMINOS',
    'ETSY', 'GOFUNDME', 'CAR WASH', 'HABIT', 'IN N OUT', 'JOE SCHMOE', 'KINDLE', 'LITTLE LADYBUG',
    'MCDONALDS', 'SHOES', 'AUTO PARTS', 'PANDA EXPRESS', 'PIEOLOGY', 'PIZZA HUT', 'AMAZON', 'APPLECOM',
    'CSC', 'GOOGLE', 'HEALTHCARE', 'TARGET', 'TRANSFER TO SHARES', 'TRANSFER FROM SHARES', 'STATERBROS',
    'STEAM', 'WALMART', 'DIVIDEND', 'TACO BELL', 'RUBIOS', 'WINGSTOP', 'SCANMOBILE', 'ZENNI OPTICAL', 'STARBUCKS', 'SIMPLE GREEK', 'HOME DEPOT',
    'ROUND TABLE', 'VOLCANO BURGER', 'TRINITY EUROPEAN', 'PAID CHECK', 'RUNNERS HIGH', 'FISH IN A BOTTLE', 'YOGURT', 'AUTOPAY AUTO-PMT', 'GAS BILL',
    'EL POLLO LOCO', 'CREDIT PAYMENT'
]

fastFood = [
    'CARLS JR', 'CHEESECAKE', 'CHICK-FIL-A', 'CHIPOTLE', 'COFFEE BEAN', 'DOMINOS', 'HABIT', 'IN N OUT', 'JOE SCHMOE', 'MCDONALDS',
    'PANDA EXPRESS', 'PIEOLOGY', 'PIZZA HUT', 'TACO BELL', 'RUBIOS', 'WINGSTOP', 'STARBUCKS', 'SIMPLE GREEK', 'ROUND TABLE', 'VOLCANO BURGER',
    'FISH IN A BOTTLE', 'YOGURT', 'EL POLLO LOCO'
]

grocery = [
    'COSTCO', 'WALMART', 'STATERBROS'
]

bills = [
    'SO CAL EDISON', 'SPECTRUM', 'T-MOBILE', 'CAR INSURANCE', 'CSC', 'GAS BILL', 'RENTERS INSURANCE', 'HEALTHCARE', 'MEDICAL'
]

car = [
    'TRINITY EUROPEAN', 'CAR WASH', 'ARCO', 'AUTO PARTS'
]

df['ChargeType'] = np.select(conditions, choices, default='NA')
df['Category'] = 'Misc'
df.loc[df['ChargeType'].isin(fastFood), 'Category'] = 'Fast Food'
df.loc[df['ChargeType'].isin(grocery), 'Category'] = 'Groceries'
df.loc[df['ChargeType'].isin(bills), 'Category'] = 'Bills'
df.loc[df['ChargeType'].isin(car), 'Category'] = 'Car'


chargeType = df.groupby(['Month', 'ChargeType'])['Total'].sum()
summary = df.groupby(['Month','Category'])['Total'].sum()

# Citi = 'Status,Date,Description,Debit,Credit,Member Name'
# NFed = "Date", "No.", "Description", "Debit", "Credit"


# print(df.groupby(['Month']).sum())
# print(df.loc[df['Description'] == 'Deposit - 0130EL12 TOTAL T'])
# print(df['Description'].unique())
# print(df.loc[df['Description'].str.contains('Amzn.com')])
# df.Description = df.Description.apply(lambda x: 'Amazon' if 'Amzn.com' in x else x)

# df['ChargeType'] = df['Description'].re.search(r'Amzn.com')
# print(df['Description'].unique())
writer = pd.ExcelWriter(refined, engine='xlsxwriter')
df.to_excel(writer, sheet_name='refined')
chargeType.to_excel(writer, sheet_name='condensed')
summary.to_excel(writer, sheet_name='Summary')
writer.close()

if directory.is_file():
    print('File exists')
    os.system(refined)
else:
    print('file does not exist')
