import FileLooper
import Extractor

fileFolder = []
InvoiceDescription = []
allInformation = []
file = ''

#get all files and add them to list
FileLooper.getFiles(fileFolder)
# print(fileFolder)
# iterate over each file and refine it from raw quickbooks pdf to information that is relavent
# for i in range(len(fileFolder)):
#     print(i)
#     fileWrite = fileFolder[i]
#     print(fileWrite)
Extractor.parseData(fileFolder, allInformation)

# Extractor.writeData(allInformation)

