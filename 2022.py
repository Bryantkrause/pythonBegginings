from asyncore import write
from distutils.log import info
import pandas as pd
import numpy as np
import re
repair = '51520 - Forklift - Repair'
file = '2022.csv'
downey = 'Henry Valdez'
fullerton = 'Luis Serrano'
rancho = 'Carlos Garcia'
cerritos = 'Frank Guzman'
columns = []
excel_file = 'MonthlySummary.xlsx'
df = pd.read_csv(file, usecols=[
    'Voucher #',
    'Date', 'Contact ID', 'Item ID', 'U/M', 'Total base',
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
choices = ['Fullerton', 'Downey', 'Cerritos', 'Rancho']
df['Location'] = np.select(locationKey, choices, default=0)

FullertonData = df.loc[df['Location'] == 'Fullerton']
CerritosData = df.loc[df['Location'] == 'Cerritos']
DowneyData = df.loc[df['Location'] == 'Downey']
RanchoData = df.loc[df['Location'] == 'Rancho']

# this entire block should be thrown in a loop as it is repetitive
pivotar = df.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Account', aggfunc='sum', values='Total base')
pivotar['Totals'] = pivotar.sum(axis=1, numeric_only=True)
pivotar.fillna(0, inplace=True)
pivotar = pivotar.sort_values(by=['Totals'], ascending=False)

fPivot = FullertonData.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Tag', aggfunc='sum', values='Total base')
fPivot['Totals'] = fPivot.sum(axis=1, numeric_only=True)
fPivot.fillna(0, inplace=True)
fPivot = fPivot.sort_values(by=['Totals'], ascending=False)

cpivot = CerritosData.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Tag', aggfunc='sum', values='Total base')
cpivot['Totals'] = cpivot.sum(axis=1, numeric_only=True)
cpivot.fillna(0, inplace=True)
cpivot = cpivot.sort_values(by=['Totals'], ascending=False)

dpivot = DowneyData.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Tag', aggfunc='sum', values='Total base')
dpivot['Totals'] = dpivot.sum(axis=1, numeric_only=True)
dpivot.fillna(0, inplace=True)
dpivot = dpivot.sort_values(by=['Totals'], ascending=False)

rpivot = RanchoData.pivot_table(columns=pd.Grouper(
    freq='M', key='Date'), index='Tag', aggfunc='sum', values='Total base')
rpivot['Totals'] = rpivot.sum(axis=1, numeric_only=True)
rpivot.fillna(0, inplace=True)
rpivot = dpivot.sort_values(by=['Totals'], ascending=False)


# with pd.ExcelWriter('MonthlySummary.xlsx') as writer:
writer = pd.ExcelWriter('MonthlySummary.xlsx', engine='xlsxwriter')

pivotar.to_excel(writer, sheet_name='Summary')
FullertonData.to_excel(writer, sheet_name='Fullerton')
fPivot.to_excel(writer, sheet_name='FullertonForks')
cpivot.to_excel(writer, sheet_name='CerritosForks')
dpivot.to_excel(writer, sheet_name='DowneyForks')
rpivot.to_excel(writer, sheet_name='RanchoForks')
writer.save()

# for col in pivotar.columns:
#     columns.append(col)
