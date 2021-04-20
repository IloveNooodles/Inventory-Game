from Save import *
import sys

def exit(filename, list):
    print("Apakah anda mau melakukan penyimpaanan file yang sudah diubah? (y/n)")
    text = input().lower()

    if text == 'y':
        save(filename, list)
    else:
        sys.exit()