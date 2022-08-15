import pandas as pd
from openpyxl import load_workbook
import datetime
import os
# grab raw data,.;p
df = pd.read_excel('ForkliftEverything.xlsx')
# split out month and year
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month

newDF = df[['Voucher #', 'Vendor', 'Quantity', 'Date',
            'U/M', 'Total', 'Account', 'Group', 'Tag', 'year', 'month']]
excel_file = 'refined.xlsx'
sheetName = 'forkliftByYear'

nForklift = newDF.groupby(['Tag', 'year','Tag'])['Total'].sum()

# check if file exists if not create it
if os.path.isfile(excel_file):
    print('removing file its for your own good')
    os.remove(excel_file)


# A working chart

writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

nForklift.to_excel(writer, sheet_name=sheetName)

workbook = writer.book
worksheet = writer.sheets[sheetName]
chart = workbook.add_chart({'type': 'scatter'})

print(len(nForklift))

max_row = len(nForklift)

col_x = 3
col_y = 1

chart.add_series({
    'name': "just Work",
    'categories': [sheetName, 1, col_x, max_row, col_x],
    'values': [sheetName, 1, col_y, max_row, col_y],
    'trendline': {'type': 'linear'},
    })
worksheet.insert_chart('C10', chart)
writer.save()

