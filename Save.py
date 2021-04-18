from Function import *
from Load import *

import os

def checkPath(folderName):
    
    Found = os.path.exists(folderName)

    if Found:
        return True 
    else:
        return False

def save(filename, list):

    folderName = input("Masukan nama Folder penyimpanan: ")

    if checkPath(folderName):
        path = os.getcwd()
        path += f"\{folderName}\{filename}"
        
        for line in list:
            writeFile(path, line)

    else:
        os.mkdir(folderName)
        path += f"\{folderName}\{filename}"

        for line in list:
            writeFile(path, line)

    print("Saving...")
    print(f"Data telah disimpan pada folder {folderName}!")

