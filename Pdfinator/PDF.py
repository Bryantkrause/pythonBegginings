import PyPDF2
import csv
# creating a pdf file object


def extractPDFData(pdfFileObj):
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    # print(f"There are this many pages: {pdfReader.numPages}")
    # creating a page object
    pageObj = pdfReader.getPage(0)
    # extracting text from page
    # print(pageObj.extractText())
    # closing the pdf file object
    # pdfFileObj.close()

    # # open the file in the write mode
    f = open(
        r'C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\csv_file.csv', 'a', newline='')

    # # create the csv writer
    writer = csv.writer(f)

    # # write a row to the csv file
    writer.writerow(pageObj.extractText())

    # # close the file
    f.close()
