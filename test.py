from Save import *
from Load import *
import sys

user = []
Folder = foundFolder()

if Folder:
    Folder = findFolder()
    user = readUser(Folder)
else:
    sys.exit()

for i in range(len(user)):
    print(lineParser(user[i]))

# print(user)
# for i in range(len(user)):
#     text = lineParser(user[i])
#     print(text)

