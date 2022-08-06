import pandas as pd
from openpyxl import load_workbook
from datetime import date

workbook = load_workbook(filename="small2.xlsx")
sheet = workbook.active

invoices = []
dates = []
vendor = []
quantity = []
unitType = []
total = []
account = []
group = []
tag = []

df = pd.read_excel('small2.xlsx')

newDF = df[['Voucher #', 'Date', 'Vendor', 'Quantity',
            'U/M', 'Total', 'Account', 'Group', 'Tag']]

newDF.to_excel(
    'refined.xlsx',
    sheet_name='panda1'
    )
