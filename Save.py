from Function import *
from Load import *

import os

def checkPath(folderName):
    
    Found = os.path.exists(folderName)

    if Found:
        return True 
    else:
        return False

def save(folderName):

    if checkPath(folderName):
        path = os.getcwd()
        path += f"\{folderName}"
        makeCsv()
    else:
        os.mkdir(folderName)
        path += f"\{folderName}"
        makeCsv()
    