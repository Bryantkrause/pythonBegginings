import re
import csv
InFin = 'Invoice#'
#len25
Description = '#DescriptionQtyRateAmount'
#len8
DescriptionEnd = 'RemitTo:'

DescriptionFind = len(Description)
DescriptonClose = len(DescriptionEnd)

def grabInfo():
    with open(r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\csv_file.csv") as x:
        reader = csv.reader(x)
        with open(r'C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\output.csv', 'w') as g:
            writer = csv.writer(g)
            for row in reader:
                new_row = [' '.join(row)]
                writer.writerow(new_row)
                #convert list intro string
                invoiceNumber = ' '.join(new_row)

                #this magic removes magical whitespace and spaces and invisible barriers
                invoiceNumberNoSpace = re.sub(
                    r"\s+", "", invoiceNumber, flags=re.UNICODE)

                # print(invoiceNumberNoSpace)
                #need to find invoice number
                invoiceFinder = invoiceNumberNoSpace.find('Invoice#')
                #This finds the invoice number and prints it
                print(invoiceNumberNoSpace[invoiceFinder +
                    len(InFin):invoiceFinder+len(InFin)+5])

                invoiceDescriptionStart = invoiceNumberNoSpace.find(Description)
                invoiceDescriptionEnd = invoiceNumberNoSpace.find(DescriptionEnd)

                print(
                    invoiceNumberNoSpace[invoiceDescriptionStart + DescriptionFind:invoiceDescriptionEnd])
