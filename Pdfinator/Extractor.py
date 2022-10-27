import enum
import pdfplumber
import csv
import re

# list of vars

invoiceList = []
fileOutPut = 'superCoolListThingy.csv'
hourLine = re.compile(r'Hour Meter: ')
unit = re.compile(r'Unit # ')
description = re.compile(r'Description Qty Rate Amount')
descriptionEnd = re.compile(r'Thank you for choosing Gold Standard Service')
descEnd = ''
descStart = ''
invoiceLine = re.compile(r'Invoice ')
descriptinator = ''
descriptionCombine = []
invoiceNumber = ''
invoiceDate = ''
meterHour = ''
unitnumber = ''
descriptionAll = []


headers = ['Invoice_Number', 'Invoice_Date',
           'Meter_Hours', 'Unit', 'Description']


def parseData(fileFolder):
    invoices= []
    dates=[]
    hours=[]
    units=[]
    descriptions=[]
    descriptionCombine.clear()


    invKey= 'Invoice_Number'
    dtKey=   'Invoice_Date'
    hrKey=   'Meter_Hours'
    unitKey=  'Unit'
    descKey=   'Description'

  
# creating a pdf file object
    for y , file in enumerate(fileFolder):
        # this is the visual to watch it do its thing
        print(y, file)
        invoiceList.append(y)

        with pdfplumber.open(file) as pdf:
            page = pdf.pages[0]
            text = page.extract_text()


        # get invoice number
        for x, line in enumerate(text.split('\n')):
            if invoiceLine.match(line):
                invoiceNum = line.lstrip("Invoice # ")
                invoices.append(invoiceNum)
                  
        # # get meter hours and row number
        for x, line in enumerate(text.split('\n')):
            if hourLine.match(line):
                rowNum, *hour = line.split()
                meterHours = re.search(r'\d+', line).group()
                hours.append(meterHours)

        # # get unit number
        for x, line in enumerate(text.split('\n')):
            if unit.match(line):
                unitNumber = line.lstrip("Unit # ").split(" ", 1)[0]
                units.append(unitNumber)


        # # get start of description line
        for start, line in enumerate(text.split('\n')):
            if description.match(line):
                descStart = start
        
        # get end of description
        for end, line in enumerate(text.split('\n')):
            if descriptionEnd.match(line):
                descEnd = end

        # clear list
        descriptionCombine.clear()

        # get only description
        for rowFind, line in enumerate(text.split('\n')):
            if descStart < rowFind and rowFind < descEnd:
                descriptionCombine.append(line)

        # combine all descriptions into one string
        descriptinator = ''.join(descriptionCombine)
        # add combined string to list to be entered
        descriptions.append(descriptinator)

        # get invoice date
        for x, line in enumerate(text.split('\n')):
            if x == 2:
                invoiceDt = re.search(r'(\d+/\d+/\d+)', line).group()
                dates.append(invoiceDt)

    # combine all lists
    newDict = [{invKey: v1, dtKey: v2, unitKey: v3, hrKey: v4, descKey: v5}
               for v1, v2, v3, v4, v5 in zip(invoices, dates, units, hours, descriptions)]

    # input parsed data into csv
    with open(fileOutPut, 'w', encoding='utf-8', newline='') as output:

        writer = csv.DictWriter(
            output, fieldnames=headers, extrasaction='ignore')
        writer.writeheader()
        for row in newDict:
            writer.writerow(row)

    


