from Load import *
from Register import * 
from Help import *
from Login import *
from Exit import *
from Save import *


import sys

user = []
gadget = []
consumables = []
gadgetBorrow = []
gadgetReturn = []
consumableHistory = []
listFile = ['user.csv', 'gadget.csv', 'gadget_return_history.csv', 'gadget_borrow_history.csv', 'consumable.csv', 'consumable_history.csv']

print()
print("Loading...")
print()

Folder = foundFolder()

if Folder:
    Folder = findFolder() 
    user = readUser(Folder)
else:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")
    sys.exit()

zipFile = [user, gadget, gadgetReturn, gadgetBorrow, consumables, consumableHistory]

while True:
    
    print()
    text = input().lower()
    print()

    if text == "login":
        login(Folder)
    elif text == "register":
        register(user)
        print(user)
    elif text == "help":
        help()
    elif text == "save":
        
        folderName = input("Masukan nama Folder penyimpanan: ")
        makeDir(folderName)

        for Csv, CsvContent in zip(listFile, zipFile):
            save(Csv, CsvContent, folderName)

        print("Saving...")
        print(f"Data telah disimpan pada folder {folderName}!")

    elif text == "exit":

        for Csv, CsvContent in zip(listFile, zipFile):
            exit(Csv, CsvContent)
