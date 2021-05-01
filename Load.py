import os
import argparse

from Function import *

parser = argparse.ArgumentParser(description="Masukan data yang akan di load")
parser.add_argument("folder", type=str)
args = parser.parse_args()

def returnFolderName():
    return args.folder

def loadFolder():
    directory = os.getcwd()
    directory += f"\{args.folder}"
    return directory

def foundFolder():
    directory = os.getcwd()
    directory = os.listdir(directory)

    if args.folder in directory:
        return True

    else:
        return False

def findFolder():
    directory = os.getcwd()
    directory = os.listdir(directory)

    if args.folder in directory:
        print(f'Selamat datang di "Kantong Ajaib!"')
        print(f"Ketik help untuk melihat list Command yang tersedia")
        return loadFolder()