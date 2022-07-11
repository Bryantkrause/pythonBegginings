import PyPDF2
import csv
# creating a pdf file object


def extractPDFData(pdfFileObj):
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    pageObj = pdfReader.getPage(0)

    # # open the file in the write mode
    f = open(
        r'C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\csv_file.csv', 'a', newline='')

    # # create the csv writer
    writer = csv.writer(f)

    # # write a row to the csv file
    writer.writerow(pageObj.extractText())

    # # close the file
    f.close()
