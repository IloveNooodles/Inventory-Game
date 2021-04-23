from Save import *
from Load import *
from Gadget import*

import sys

consumables = []
Folder = foundFolder()

if Folder:
    Folder = findFolder()
else:
    sys.exit()

consumables = readConsumables(Folder)

id = input()

hapusitem(consumables, id)

# print(consumables)





