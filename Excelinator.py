import pandas as pd
from openpyxl import load_workbook
import datetime
import os
# grab raw data,.;p
df = pd.read_excel('ForkliftEverything.xlsx')
# split out month and year
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
excel_file = 'refined.xlsx'
sheetName = 'chartyMcChartFace'


newDF = df[['Voucher #', 'Vendor', 'Quantity', 'Date',
            'U/M', 'Total', 'Account', 'Group', 'Tag', 'year', 'month']]

print(newDF.info())
# print(newDF.info())
# summary by invoice
total = newDF.groupby(['Voucher #', 'Date', 'Tag'])['Total', 'Quantity'].sum()

# summary by month
monthly = newDF.groupby(['Date', 'year', 'month'])[
    'Total', 'Quantity'].sum()

# summary by forklift
forklift = newDF.groupby(['Tag', 'year', 'month'])['Total', 'Quantity'].sum()

nForklift = newDF.groupby(['Tag', 'year'])['Total'].sum()
print(nForklift.head())
# check if file exists if not create it
if os.path.isfile(excel_file):
    print('removing file its for your own good')
    os.remove(excel_file)
    with pd.ExcelWriter(excel_file) as writer:
        total.to_excel(writer, sheet_name='Refined')
        monthly.to_excel(writer, sheet_name='byMonth')
        forklift.to_excel(writer, sheet_name='byForklift')
        newDF.to_excel(writer, sheet_name='panda1')
        nForklift.to_excel(writer, sheet_name='forkliftByYear')

        workbook = writer.book
        worksheet = nForklift.to_excel(writer, sheet_name=sheetName)
        chart = workbook.add_chart({'type': 'column'})
        max_row = nForklift.iloc[-1]
        chart.add_series({'values': [sheetName, 1, 1, max_row, 1]})
        worksheet.insert_chart(1, 3, chart)
        writer.save()
else:
    print('creating file without deleting it')
    with pd.ExcelWriter(excel_file) as writer:
        total.to_excel(writer, sheet_name='Refined')
        monthly.to_excel(writer, sheet_name='byMonth')
        forklift.to_excel(writer, sheet_name='byForklift')
        newDF.to_excel(writer, sheet_name='panda1')
        nForklift.to_excel(writer, sheet_name='forkliftByYear')


def makeChart():
    print('making your chart')
