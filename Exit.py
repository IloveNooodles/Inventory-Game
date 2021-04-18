from Save import *
import sys

def exit(folderName, filename, list):
    print("Apakah anda mau melakukan penyimpaanan file yang sudah diubah? (y/n)")
    text = input().lower()

    if text == 'y':
        save(folderName, filename, list)
    else:
        sys.exit()