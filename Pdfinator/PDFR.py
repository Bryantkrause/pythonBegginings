import FileLooper
import Extractor

fileFolder = []
InvoiceDescription = []
allInformation = []
file = ''

#get all files and add them to list
FileLooper.getFiles(fileFolder)
Extractor.parseData(fileFolder)


