from Save import *
import sys

def exit(filename, list, folderName, text):
    if text == 'y':
        save(filename, list, folderName)
    else:
        sys.exit()