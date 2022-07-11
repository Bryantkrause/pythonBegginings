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
#get all files and add them to list
FileLooper.getFiles(fileFolder)

# iterate over each file and refine it from raw quickbooks pdf to information that is relavent
for i in range(len(fileFolder)):
    print(i)
    pdfFileObj = fileFolder[i]
    PDF.extractPDFData(pdfFileObj)
TextGrabber.grabInfo(InvoiceDescription)
