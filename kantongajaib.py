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
zipFile = [user, gadget, gadgetReturn, gadgetBorrow, consumables, consumableHistory]

print()
print("Loading...")
print()

Folder = foundFolder()

if Folder:
    Folder = findFolder()
    print(Folder)
else:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")
    sys.exit()

while True:
    
    print()
    text = input()
    print()

    if text == "login":
        login()
    elif text == "register":
        user = register()
    elif text == "help":
        help()
    elif text == "save":

        for Csv, CsvContent in zip(listFile, zipFile):
            save(Csv, CsvContent)

    elif text == "exit":

        for Csv, CsvContent in zip(listFile, zipFile):
            exit(Csv, CsvContent)
