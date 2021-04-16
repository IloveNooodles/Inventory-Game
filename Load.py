import os
import argparse

parser = argparse.ArgumentParser(description="Masukan data yang akan di load")
parser.add_argument("folder", type=str)
args = parser.parse_args()

def loadFolder():
    directory = os.getcwd()
    directory += f"\{args.folder}"
    return directory

def findFolder():
    directory = os.getcwd()
    directory = os.listdir(directory)
    if args.folder in directory:
        loadFolder()
        print(f'Selamat datang di "Kantong Ajaib!"')
    else:
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python kantongajaib.py <nama_folder>")


