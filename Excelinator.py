import pandas as pd
from openpyxl import load_workbook
import datetime
import os
# grab raw data
df = pd.read_excel('ForkliftEverything.xlsx')
# split out month and year
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month

excel_file = 'refined.xlsx'
sheet_name = 'chartyMcChartFace'



newDF = df[['Voucher #', 'Vendor', 'Quantity','Date',
            'U/M', 'Total', 'Account', 'Group', 'Tag','year','month' ]]

print(newDF.info())
# print(newDF.info())
# summary by invoice
total = newDF.groupby(['Voucher #','Date', 'Tag'])['Total', 'Quantity'].sum()

# summary by month
monthly = newDF.groupby([ 'Date','year', 'month'])[
    'Total', 'Quantity'].sum()

# summary by forklift
forklift = newDF.groupby(['Tag', 'year', 'month'])['Total','Quantity'].sum()

nForklift = newDF.groupby(['Tag', 'year'])['Total'].sum()

# check if file exists if not create it
if os.path.isfile('./refined.xlsx'):
    print('removing file its for your own good')
    os.remove('./refined.xlsx')
    with pd.ExcelWriter('refined.xlsx') as writer:
        total.to_excel(writer, sheet_name='Refined')
        monthly.to_excel(writer, sheet_name='byMonth')
        forklift.to_excel(writer, sheet_name='byForklift')
        newDF.to_excel(writer, sheet_name='panda1')
        nForklift.to_excel(writer, sheet_name='forkliftByYear')
else:
    print('creating file without deleting it')
    with pd.ExcelWriter('refined.xlsx') as writer:
        total.to_excel(writer, sheet_name='Refined')
        monthly.to_excel(writer, sheet_name='byMonth')
        forklift.to_excel(writer, sheet_name='byForklift')
        newDF.to_excel(writer, sheet_name='panda1')


def makeChart():
    print('making your chart')
