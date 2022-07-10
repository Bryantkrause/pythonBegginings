import PyPDF2
import csv
import os
import string
import FileLooper
import PDF
import TextGrabber
fileFolder = []
InvoiceDescription = []
pdfFileObj = ''
FileLooper.getFiles(fileFolder)

for i in range(len(fileFolder)):
    print(i)
    pdfFileObj = fileFolder[i]
    PDF.extractPDFData(pdfFileObj)
TextGrabber.grabInfo(InvoiceDescription)
