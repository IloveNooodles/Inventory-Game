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

item = gadget[2]['jumlah']
print(type(item))

item = int(item)
print(type(item))

print(item)

id = input()

ubahItem(gadget, id)

print(gadget)





