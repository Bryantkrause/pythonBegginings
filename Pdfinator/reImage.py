import enum
import pdfplumber
import csv
import re

from Old import Description, DescriptionEnd
# creating a pdf file object

file = f'.//Files//36907.pdf'

with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# print testing for testifying
# print(text)
# for x, line in enumerate(text.split('\n')):
#     print(x, line)
# get invoice number
invoiceLine = re.compile(r'Invoice ')


for line in text.split('\n'):
    if invoiceLine.match(line):
        invoiceNumber = line.lstrip("Invoice # ")
        print(f"invoice number is: {invoiceNumber}")

# get meter hours and row number
hourLine = re.compile(r'Hour Meter: ')

for x, line in enumerate(text.split('\n')):
    if hourLine.match(line):
        rowNum, *hours = line.split()
        meterHours = re.search(r'\d+', line).group()
        print(x, f" meter hours are: {meterHours}")

# get unit number
unit = re.compile(r'Unit # ')

for x, line in enumerate(text.split('\n')):
    if unit.match(line):
        unitNumber = line.lstrip("Unit # ").split(" ", 1)[0]
        print(x, f"unit number is: {unitNumber}")

description = re.compile(r'Description Qty Rate Amount')

descStart = ''
for x, line in enumerate(text.split('\n')):
    if description.match(line):
        print(x,  line)
        descStart = x
print(descStart)

descriptionEnd = re.compile(r'Thank you for choosing Gold Standard Service')

descEnd = ''
for x, line in enumerate(text.split('\n')):
    if descriptionEnd.match(line):
        print(x,  line)
        descEnd = x
print(descEnd)

for x, line in enumerate(text.split('\n')):
    if descStart < x and x < descEnd:
        print(x , line)


    #     startRow = description.match(line)
    # if startRow is None:
    #     startRow = 0

    # if x > 15:
        
