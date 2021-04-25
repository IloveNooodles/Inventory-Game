from Save import *
from Load import *
from Gadget import*
from Function import *

import sys

Folder = foundFolder()

if Folder:
    Folder = findFolder()
else:
    sys.exit()

consumableHistory = readConsumableHistory(Folder)
consumable = readConsumables(Folder)
user = readUser(Folder)

RiwayatAmbilConsumables(consumableHistory, user, consumable)






