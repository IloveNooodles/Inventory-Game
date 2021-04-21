from Save import *
from Load import *
from Gadget import*

import sys

gadget = []
Folder = foundFolder()

if Folder:
    Folder = findFolder()
else:
    sys.exit()

gadget = readGadget(Folder)

tahun = int(input("masukan thaun: "))
op = input("operator: ")

print()
print("Hasil pencarian: ")
print()


cariTahun(tahun, op, gadget[1:])




# for i in range(len(gadget)):
#     print(lineParser(gadget[i]))

