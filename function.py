import os
import sys
import argparse
import datetime

from consumables import *
from Gadget import *

def makeCsv(): #membuat csv dari fucntion, cuma kepake sekali
    filename = "data/user.csv"
    with open (filename, 'w') as file:
        file.write("id;username;nama;alamat;password;role")
    
    filename = "data/gadget.csv"
    with open (filename, 'w') as file:
        file.write("id;nama;deskripsi;jumlah;rarity;tahun_ditemukan")
    
    filename = "data/consumable.csv"
    with open (filename, 'w') as file:
        file.write("id;nama;deskripsi;jumlah;rarity")
    
    filename = "data/consumable_history.csv"
    with open (filename, 'w') as file:
        file.write("id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah")
    
    filename = "data/gadget_borrow_history.csv"
    with open (filename, 'w') as file:
        file.write("id;id_peminjam;id_gadget;tanggal_peminjaman;jumlah")
    
    filename = "data/gadget_return_history.csv"
    with open (filename, 'w') as file:
        file.write("id;id_pengambil;id_gadget;tanggal_peminjaman;jumlah")

def readFile(filename):
    with open (filename, 'r') as file:
        contents = file.read()

def writeFile(filename, text):
    with open(filename, 'w') as file:
        file.write(f"{text}\n")

def appendFile(filename, text):
    with open(filename, 'a') as file:
        file.write(f"{text}\n")

def checkFunction(list, checkItem):
    for item in list:
        if item == checkItem :
            return True

def searchFunction(list, checkItem, message):
    idx = -1
    for i in range(len(list)):
        if checkItem == checkItem:
            idx = i
            break
    if idx == -1:
        return f"{message}"
    else:
        return idx

def CSVParser(lines): #Memparse bentuk CSV ke dalam bentuk list
    listReturn = []
    text = ''
    idx = 1

    for char in lines:
        if char == ';' or char == '\n':
            listReturn.append(text)
            text = ''
        elif idx == len(lines):
            text += char
            listReturn.append(text)
        else:
            text += char
            
        idx += 1

    return listReturn

def lineParser(list):
    
    text = ''

    for item in list:
        text += list.get(item)
        text += ';'
    text = text[:-1]   

    return text

def toCSV(path, list):
    text = lineParser(list)
    appendFile(path, lineParser(list))

def makeList(list, keyword):

    newList = []

    for i in range(len(list)):
        newList.append(list[i][keyword])
    
    return newList

def readUser(folder):
    user = []
    filename = folder
    filename += "\\user.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempUser = CSVParser(line)
            dict["id"] = tempUser[0]
            dict["username"] = tempUser[1]
            dict["nama"] = tempUser[2]
            dict["alamat"] = tempUser[3]
            dict["password"] = tempUser[4]
            dict["role"] = tempUser[5]

            user.append(dict)

    return user

def readGadget(folder):
    gadget = []
    filename = folder
    filename += "\\gadget.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempUser = CSVParser(line)
            dict["id"] = tempUser[0]
            dict["nama"] = tempUser[1]
            dict["deskripsi"] = tempUser[2]
            dict["jumlah"] = tempUser[3]
            dict["rarity"] = tempUser[4]
            dict["tahun_ditemukan"] = tempUser[5]

            gadget.append(dict)

    return gadget

def readConsumables(folder):
    array = []
    filename = folder
    filename += "\\consumable.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempArray = CSVParser(line)
            dict["id"] = tempArray[0]
            dict["nama"] = tempArray[1]
            dict["deskripsi"] = tempArray[2]
            dict["jumlah"] = tempArray[3]
            dict["rarity"] = tempArray[4]

            array.append(dict)

    return array

def readConsumableHistory(folder):
    array = []
    filename = folder
    filename += "\\consumable_history.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempArray = CSVParser(line)
            dict["id"] = tempArray[0]
            dict["id_pengambil"] = tempArray[1]
            dict["id_consumable"] = tempArray[2]
            dict["tanggal_pengambilan"] = tempArray[3]
            dict["jumlah"] = tempArray[4]

            array.append(dict)

    return array

def readGadgetBorrow(folder):
    array = []
    filename = folder
    filename += "\\gadget_borrow_history.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempArray = CSVParser(line)
            dict["id"] = tempArray[0]
            dict["id_peminjam"] = tempArray[1]
            dict["id_gadget"] = tempArray[2]
            dict["tanggal_peminjaman"] = tempArray[3]
            dict["jumlah"] = tempArray[4]
            dict["is_returned"] = tempArray[5]

            array.append(dict)

    return array

def readGadgetReturn(folder):
    array = []
    filename = folder
    filename += "\\gadget_return_history.csv"

    with open(filename, "r") as file:
        for line in file:
            dict = {}
            tempArray = CSVParser(line)
            dict["id"] = tempArray[0]
            dict["id_peminjaman"] = tempArray[1]
            dict["tanggal_pengembalian"] = tempArray[2]
            dict["jumlah_peminjaman"] = tempArray[3]

            array.append(dict)

    return array

def tambahItem(list, id):

    if id[0] == 'G':
        tambahGadget(list, id)
    elif id[0] == 'C':
        tambahConsumables(list, id)
    else:
        print("Gagal menambahkan item karena ID tidak valid")

def hapusitem(list, id):
    if id[0] == 'G':
        hapusGadget(list, id)
    elif id[0] == 'C':
        hapusConsumables(list, id)
    else:
        print("Gagal menghapus item karena ID tidak valid")

def ubahItem(list, id):
    if id[0] == 'G':
        ubahGadget(list, id)
    elif id[0] == 'C':
        ubahConsumables(list, id)
    else:
        print("Gagal mengubah item karena ID tidak valid")