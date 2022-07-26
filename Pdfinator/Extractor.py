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
descriptionCombine = []
descriptinator = ''
invoiceNumber = ''
invoiceDate = ''
meterHour = ''
unitnumber = ''
descriptionAll = ''



headers = ['Invoice_Number', 'Invoice_Date',
           'Meter_Hours', 'Unit', 'Description']


def parseData(fileFolder, allInformation):
    invoices= []
    dates=[]
    hours=[]
    units=[]
    descriptions=[]


    invKey= 'Invoice_Number'
    dtKey=   'Invoice_Date'
    hrKey=   'Meter_Hours'
    unitKey=  'Unit'
    descKey=   'Description'

  
# creating a pdf file object
    for y , file in enumerate(fileFolder):
        invoiceList.append(y)
        print(y, file)
        # print(f"this is what i need{x}" ,file)
        with pdfplumber.open(file) as pdf:
            # print(file)
            page = pdf.pages[0]
            text = page.extract_text()


        # get invoice number
        for x, line in enumerate(text.split('\n')):
            if invoiceLine.match(line):
                invoiceNum = line.lstrip("Invoice # ")
                invoices.insert(x, invoiceNum)
                
                
        # # get meter hours and row number
        for x, line in enumerate(text.split('\n')):
            if hourLine.match(line):
                rowNum, *hour = line.split()
                meterHours = re.search(r'\d+', line).group()
                hours.insert(x, meterHours)

        # # get unit number
        for x, line in enumerate(text.split('\n')):
            if unit.match(line):
                unitNumber = line.lstrip("Unit # ").split(" ", 1)[0]
                units.insert(x, unitNumber)


        # # get start of description line
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

        # # get only description
        for x, line in enumerate(text.split('\n')):
            if descStart < x and x < descEnd:
                # print(x , line)
                descriptionCombine.append(line)
                # print(descriptionCombine)

        descriptinator = ''.join(descriptionCombine)

        descriptions.insert(y, descriptinator)



        for x, line in enumerate(text.split('\n')):
            if x == 2:
                # print(line)
                # invoiceDt = re.search('([0-9]\/[0-9]\/[0-9])', line).group()
                invoiceDt = re.search(r'(\d+/\d+/\d+)', line).group()
                dates.append(invoiceDt)
        print(invoices)
        print(hours)
        print(units)
        print(dates)
        print(len(descriptions))

    newDict = [{invKey: v1, dtKey: v2, unitKey: v3, hrKey: v4, descKey: v5}
               for v1, v2, v3, v4, v5 in zip(invoices, dates, units, hours, units)]
    print(newDict)
    


    
        



# def writeData(allInformation):
#     # print(allInformation)
#     with open(fileOutPut, 'w', encoding='utf-8', newline='') as output:
#         # print(allInformation)
#         writer = csv.DictWriter(
#             output, fieldnames=headers, extrasaction='ignore')
#         writer.writeheader()
#         for row in allInformation:
#             # print(f" this is the row that is being writting {row}")
#             writer.writerow(row)

    


