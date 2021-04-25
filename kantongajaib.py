from Load import *
from Register import * 
from Help import *
from Login import *
from Exit import *
from Save import *
from Gadget import *
from consumables import *

import sys

user = []
gadget = []
consumables = []
gadgetBorrow = []
gadgetReturn = []
consumableHistory = []
listFile = ['user.csv', 'gadget.csv', 'gadget_return_history.csv', 'gadget_borrow_history.csv', 'consumable.csv', 'consumable_history.csv']

print()
print("Loading...")
print()

Folder = foundFolder()
UserFile = ''
idUser = ''
roleUser = ''

if Folder:
    Folder = findFolder() 
    user = readUser(Folder)
    gadget = readGadget(Folder)
    gadgetBorrow = readGadgetBorrow(Folder)
    gadgetReturn = readGadgetReturn(Folder)
    consumables = readConsumables(Folder)
    consumableHistory = readConsumableHistory(Folder)
else:
    print("Tidak ada nama folder yang diberikan!")
    print("Usage: python kantongajaib.py <nama_folder>")
    sys.exit()

zipFile = [user, gadget, gadgetReturn, gadgetBorrow, consumables, consumableHistory]

while True:
    
    print()
    text = input().lower()
    print()

    if text == "login":
        userFile = login(Folder)
        idUser = str(userFile[0])
        roleUser = userFile[1]

    elif text == "register":
        register(user)

    elif text == 'carirarity':
        searchRarity = input("Masukan Rarity: ")
        cariRarity(gadget, searchRarity)
    
    elif text == 'caritahun':
        tahun = int(input("Masukan Tahun: "))
        kategori = input("Masukan kategori: ")
        cariTahun(tahun, kategori, gadget)

    elif text == "tambahitem":
        id = input("Masukan ID: ")
        if id[0] == 'G':
            tambahItem(gadget, id)
        elif id[0] == 'C':
            tambahItem(consumables, id)
        
    elif text == "hapusitem":
        id = input("Masukan ID item: ")
        if id[0] == 'G':
            hapusitem(gadget, id)
        elif id[0] == 'C':
            hapusitem(consumables, id)

    elif text == "ubahitem":
        id = input("Masukan ID item: ")
        if id[0] == 'G':
            ubahItem(gadget, id)
        elif id[0] == 'C':
            ubahItem(consumables, id)
    
    elif text == 'pinjam':
        id = input("Masukan ID item: ")
        pinjamGadget(gadget, gadgetBorrow, id, idUser)
    
    elif text == 'kembalikan':
        mengembalikanGadget(gadget, gadgetBorrow, gadgetReturn, idUser)

    elif text == 'minta':
        id = input("Masukan ID item: ")
        memintaConsumables(consumables, consumableHistory, id, idUser)

    elif text == 'riwayatpinjam':
        RiwayatPinjamGadget(gadgetBorrow, user, gadget)
    
    elif text == 'riwayatkembali':
        RiwayatReturnGadget(gadgetReturn, gadgetBorrow, user, gadget)

    elif text == 'riwayatambil':
        RiwayatAmbilConsumables(consumableHistory, user, consumables)

    elif text == "help":
        help()

    elif text == "save":
        
        folderName = input("Masukan nama Folder penyimpanan: ")
        makeDir(folderName)

        for Csv, CsvContent in zip(listFile, zipFile):
            save(Csv, CsvContent, folderName)

        print("Saving...")
        print(f"Data telah disimpan pada folder {folderName}!")

    elif text == "exit":
        print("Apakah anda mau melakukan penyimpaanan file yang sudah diubah? (y/n)")
        text = input().lower()

        if text == 'n':
            sys.exit()

        folderName = returnFolderName()
        makeDir(folderName)

        for Csv, CsvContent in zip(listFile, zipFile):
            exit(Csv, CsvContent, folderName, text)
        
        sys.exit()

