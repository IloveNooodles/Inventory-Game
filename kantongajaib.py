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
        if roleUser == 'admin':
            register(user)
        else:
            print("Hanya admin yang bisa register")

    elif text == 'carirarity':
        searchRarity = input("Masukan Rarity: ")
        print()
        cariRarity(gadget, searchRarity)
    
    elif text == 'caritahun':
        tahun = int(input("Masukan Tahun: "))
        kategori = input("Masukan kategori: ")
        print()
        cariTahun(tahun, kategori, gadget)

    elif text == "tambahitem":
        if roleUser == 'admin':
            id = input("Masukan ID: ")
            if id[0] == 'G':
                tambahItem(gadget, id)
            elif id[0] == 'C':
                tambahItem(consumables, id)
        else:
            print("Hanya Admin yang bisa menambah item")
        
    elif text == "hapusitem":
        if roleUser == 'admin':
            id = input("Masukan ID item: ")
            if id[0] == 'G':
                hapusitem(gadget, id)
            elif id[0] == 'C':
                hapusitem(consumables, id)
        else:
            print("Hanya Admin yang bisa menghapus item")

    elif text == "ubahitem":
        if roleUser == 'admin':
            id = input("Masukan ID item: ")
            if id[0] == 'G':
                ubahItem(gadget, id)
            elif id[0] == 'C':
                ubahItem(consumables, id)
        else:
            print("Hanya admin yang bisa mengubah item")
    
    elif text == 'pinjam':
        if roleUser == 'user':
            id = input("Masukan ID item: ")
            pinjamGadget(gadget, gadgetBorrow, id, idUser)
        else:
            print("Hanya user yang bisa meminjam gadget")
    
    elif text == 'kembalikan':
        if roleUser == 'user':
            mengembalikanGadget(gadget, gadgetBorrow, gadgetReturn, idUser)
        else:
            print("Hanya user yang bisa mengembalikan gadget")

    elif text == 'minta':
        if roleUser == 'user':
            id = input("Masukan ID item: ")
            memintaConsumables(consumables, consumableHistory, id, idUser)
        else:
            print("Hanya user yang bisa meminjam gadget")

    elif text == 'riwayatpinjam':
        if roleUser == 'admin':
            RiwayatPinjamGadget(gadgetBorrow, user, gadget)
        else:
            print("Hanya admin yang bisa melihat riwayat pinjam")

    elif text == 'riwayatkembali':
        if roleUser == 'admin':
            RiwayatReturnGadget(gadgetReturn, gadgetBorrow, user, gadget)
        else:
            print("Hanya admin yang bisa melihat riwayat kembali")

    elif text == 'riwayatambil':
        if roleUser == 'admin':
            RiwayatAmbilConsumables(consumableHistory, user, consumables)
        else:
            print("Hanya admin yang bisa melihat riwayat ambil")

    elif text == "help":
        if roleUser == 'admin':
            help(1)
        else:
            help(2)

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

