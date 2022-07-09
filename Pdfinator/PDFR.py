import PyPDF2
import csv
import os
import string

path = r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator"
dirs = os.listdir(path)
# creating a pdf file object
pdfFileObj = open(
    r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\Files\36907.pdf", 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# printing number of pages in pdf file
print(f"There are this many pages: {pdfReader.numPages}")
# creating a page object
pageObj = pdfReader.getPage(0)
# extracting text from page
print(pageObj.extractText())
# closing the pdf file object
pdfFileObj.close()

invoiceDetail = []
# # open the file in the write mode
f = open(r'C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\output.csv', 'w')

# # create the csv writer
writer = csv.writer(f)

# # write a row to the csv file
# writer.writerow(pageObj.extractText())

# # close the file
f.close()


# find start of invoice #
import re

for file in dirs:
    print(file)

with open(r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\csv_file.csv") as x:
    reader = csv.reader(x)
    with open(r'C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\output.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [' '.join(row)]
            writer.writerow(new_row)
            invoiceNumber = ' '.join(new_row)
            # print(invoiceNumber)
            invoiceNumberNoSpace = re.sub(r"\s+", "", invoiceNumber, flags=re.UNICODE)
            # invoiceNumber.replace(" ","")
            print(invoiceNumberNoSpace)
            invoiceFinder = invoiceNumber.find('Invoice#')
            # print(invoiceNumber.find('3 6 9 0 7'))
            # print(invoiceFinder)
