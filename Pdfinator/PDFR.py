import FileLooper
import Extractor

fileFolder = []

#get all files and add them to list
FileLooper.getFiles(fileFolder)
print(fileFolder)
Extractor.parseData(fileFolder)


