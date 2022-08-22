from distutils.log import info
import pandas as pd
import numpy as np
import re
repair = '51520 - Forklift - Repair'
file ='2022.csv'
downey = 'Henry Valdez'
fullerton = 'Luis Serrano'
rancho = 'Carlos Garcia'
cerritos = 'Frank Guzman'
columns = []
df = pd.read_csv(file, usecols=[
    'Voucher #',
    'Date','Contact ID','Item ID','U/M','Total base',
    'Account', 'Group', 'Tag', 'Memo', 'Approvers'], parse_dates=['Date'], na_values=0)

print(df['Account'])
df.fillna(0, inplace=True)
df['aClean'] = df['Approvers'].str.split('(').str[0].str.rstrip()

locationKey = [
    (df['aClean'] == fullerton) & (df['Account'] == repair),
    (df['aClean'] == downey) & (df['Account'] == repair),
    (df['aClean'] == cerritos) & (df['Account'] == repair),
    (df['aClean'] == rancho) & (df['Account'] == repair)
]
choices = ['Fullerton','Downey','Cerritos','Rancho']
df['Location'] = np.select(locationKey, choices, default=0)

FullertonData = df.loc[df['Location'] == 'Fullerton']

pivotar = df.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Account', aggfunc='sum', values='Total base')
pivotar['Totals'] = pivotar.sum(axis=1, numeric_only=True)
# for col in pivotar.columns:
#     columns.append(col)
pivotar.fillna(0,inplace=True)

fPivot = FullertonData.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Tag', aggfunc='sum', values='Total base')
fPivot['Totals'] = fPivot.sum(axis=1, numeric_only=True)
fPivot.fillna(0, inplace=True)
with pd.ExcelWriter('MonthlySummary.xlsx') as writer:
    pivotar.to_excel(writer, sheet_name='Summary')
    FullertonData.to_excel(writer, sheet_name='Fullerton')
    fPivot.to_excel(writer, sheet_name='FullertonForks')


