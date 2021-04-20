from Function import *
from Load import *

import os

def checkPath(folderName):
    
    Found = os.path.exists(folderName)

    if Found:
        return True 
    else:
        return False

def makeDir(folderName):
    listFile = ['user.csv', 'gadget.csv', 'gadget_return_history.csv', 'gadget_borrow_history.csv', 'consumable.csv', 'consumable_history.csv']

    if checkPath(folderName):
        for folder, subfolder, files in os.walk(folderName):
            for file in files:
                if file in listFile:
                    path = os.path.join(folderName, file)
                    os.remove(path)
                    
    else:
        os.mkdir(folderName)

def save(filename, list, folderName):
    path = os.getcwd()
    path += f"\{folderName}\{filename}"

    for i in range(len(list)):
        toCSV(path, list[i])

    

