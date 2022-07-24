import pdfplumber
import csv
import re
# creating a pdf file object

file = f'.//Files//36907.pdf'

with pdfplumber.open(file) as pdf:
    page = pdf.pages[0]
    text = page.extract_text()

# print(text)
# get invoice number
invoiceLine = re.compile(r'Invoice ')

for line in text.split('\n'):
    if invoiceLine.match(line):
        print(line.lstrip("Invoice # "))

# get meter hours and row number
hourLine = re.compile(r'Hour Meter: ')

for x, line in enumerate(text.split('\n')):
    if hourLine.match(line):
        print(x, re.search(r'\d+', line).group())
