import os

# path = r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator"


def getFiles(fileFolder):
    
   #  directory = r"C:\Users\bryan\Desktop\rebirth\pythonBeginings\Pdfinator\Files"
    directory = r'\\appserver2k8\finance\2022 Finance\BK\Spendwise\GoldStandard2022'
    # iterate over all files in directory
    for filename in os.listdir(directory):
       f = os.path.join(directory, filename)
       # checking if it is a file
       if os.path.isfile(f):
          # print(f)
          fileFolder.append(f) 
      
          

