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
returnGadget = readGadgetReturn(Folder)
borrowGadget = readGadgetBorrow(Folder)

print(gadget, returnGadget, borrowGadget)

mengembalikanGadget(gadget, borrowGadget, returnGadget, "1")

print(gadget, returnGadget, borrowGadget)
