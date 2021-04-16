from Load import *
from Register import * 
from Help import *
from Login import *

import sys

print("Loading...")
print()

Folder = foundFolder()

if Folder:
    Folder = findFolder()
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