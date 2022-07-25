import enum
import pdfplumber
import csv
import re

from Old import Description, DescriptionEnd

# list of vars
file = f'.//Files//36908.pdf'
invoiceList = []
hourLine = re.compile(r'Hour Meter: ')
unit = re.compile(r'Unit # ')
description = re.compile(r'Description Qty Rate Amount')
descriptionEnd = re.compile(r'Thank you for choosing Gold Standard Service')
descEnd = ''
descStart = ''
invoiceLine = re.compile(r'Invoice ')
descriptionCombine = []
descriptinator = ''
# creating a pdf file object
with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# print testing for testifying
# print(text)
# for x, line in enumerate(text.split('\n')):
#     print(x, line)


# get invoice number
for line in text.split('\n'):
    if invoiceLine.match(line):
        invoiceNumber = line.lstrip("Invoice # ")
        print(f"invoice number is: {invoiceNumber}")

# get meter hours and row number
for x, line in enumerate(text.split('\n')):
    if hourLine.match(line):
        rowNum, *hours = line.split()
        meterHours = re.search(r'\d+', line).group()
        print(x, f" meter hours are: {meterHours}")

# get unit number
for x, line in enumerate(text.split('\n')):
    if unit.match(line):
        unitNumber = line.lstrip("Unit # ").split(" ", 1)[0]
        print(x, f"unit number is: {unitNumber}")



# get start of description line
for x, line in enumerate(text.split('\n')):
    if description.match(line):
        # print(x,  line)
        descStart = x
# print(descStart)

# get end of description
for x, line in enumerate(text.split('\n')):
    if descriptionEnd.match(line):
        # print(x,  line)
        descEnd = x
# print(descEnd)

# get only description
for x, line in enumerate(text.split('\n')):
    if descStart < x and x < descEnd:
        # print(x , line)
        descriptionCombine.append(line)
        # print(descriptionCombine)

descriptinator =''.join(descriptionCombine)
print(descriptinator)

for x, line in enumerate(text.split('\n')):
    if x == 2:
        # print(line)
        invoiceDate = re.search('([0-9]\/[0-9]\/[0-9]{4})', line).group()
        print(f"Invoice date is: {invoiceDate}")
