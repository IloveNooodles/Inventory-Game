import datetime
from Function import *

def sortDateTimeGadget(list):
    list.sort(key = lambda date : datetime.datetime.strptime(date, "%d/%m/%Y"), reverse = True)
    return list

def GadgetCsvParser(lines): #Memparse bentuk CSV ke dalam bentuk list
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

def lineParserGadget(list):

    text = ''

    for item in list:
        text += list.get(item)
        text += ';'
    text = text[:-1]   

    return text


def formatGadget(list):

    nama = list[1]
    deskripsi = list[2]
    jumlah = list[3]
    rarity = list[4]
    tahunDitemukan = list[5]

    print(f"Nama\t\t: {nama}")
    print(f"Deskripsi\t: {deskripsi}")
    print(f"Jumlah\t\t: {jumlah} buah")
    print(f"Rarity\t\t: {rarity}")
    print(f"Tahun Ditemukan\t: {tahunDitemukan}")
    print()

def formatPinjamGadget(list):
    
    counter = 0

    for i in range(len(list)):

        counter += 1

        idPeminjaman = list[i][0]
        namaPengambil = list[i][1]
        NamaGadget = list[i][2]
        TanggalPeminjaman = list[i][3]
        Jumlah = str(list[i][4])

        print(f"ID Peminjaman\t\t: {idPeminjaman}")
        print(f"Nama Pengambil\t\t: {namaPengambil}")
        print(f"Nama Gadget\t\t: {NamaGadget}")
        print(f"Tanggal Peminjaman\t: {TanggalPeminjaman}")
        print(f"Jumlah\t\t\t: {Jumlah}")
        print()

        if i == len(list):
            break

        if counter%5 == 0:
            text = input("Apakah ingin dilanjutkan (Y/N)? ").upper()
            if text == 'N':
                break

            print()

def formatReturnGadget(list):
    
    counter = 0

    for i in range(len(list)):

        counter += 1

        idPengembalian = list[i][0]
        namaPengambil = list[i][1]
        NamaGadget = list[i][2]
        TanggalPeminjaman = list[i][3]
        Jumlah = str(list[i][4])

        print(f"ID Pengembalian\t\t: {idPengembalian}")
        print(f"Nama Pengambil\t\t: {namaPengambil}")
        print(f"Nama Gadget\t\t: {NamaGadget}")
        print(f"Tanggal Pengembalian\t: {TanggalPeminjaman}")
        print(f"Jumlah peminjaman\t: {Jumlah}")
        print()

        if i == len(list):
            break

        if counter%5 == 0:
            text = input("Apakah ingin dilanjutkan (Y/N)? ").upper()
            if text == 'N':
                break

            print()

def RiwayatPinjamGadget(listBorrowGadget, listUser, listGadget):
    
    index = returnIndexBorrowGadgetDate(listBorrowGadget)

    idpeminjam = []
    namaPengambil = []
    idGadget = []
    idpinjam = []
    namaGadget = []
    tanggal = []
    jumlah = []

    for i in range(len(index)):
        idpeminjam.append(listBorrowGadget[index[i]]['id_peminjam'])
        idGadget.append(listBorrowGadget[index[i]]['id_gadget'])
        idpinjam.append(listBorrowGadget[index[i]]['id'])
        tanggal.append(listBorrowGadget[index[i]]['tanggal_peminjaman'])
        jumlah.append(listBorrowGadget[index[i]]['jumlah'])
    
    for i in range(len(idpeminjam)):
        for j in range(1, len(listUser)):
            if idpeminjam[i] == listUser[j]['id']:
                namaPengambil.append(listUser[j]['nama'])
    
    for i in range(len(idGadget)):
        for j in range(1, len(listGadget)):
            if idGadget[i] == listGadget[j]['id']:
                namaGadget.append(listGadget[j]['nama'])

    listTempAll = []

    for i in range(len(idpinjam)):
        tempAll = []
        tempAll.append(idpinjam[i])
        tempAll.append(namaPengambil[i])
        tempAll.append(namaGadget[i])
        tempAll.append(tanggal[i])
        tempAll.append(jumlah[i])
        listTempAll.append(tempAll)

    formatPinjamGadget(listTempAll)

def RiwayatReturnGadget(listReturnGadget, listBorrowGadget, listUser, listGadget):
    
    index = returnIndexReturnGadgetDate(listReturnGadget)
    idpeminjaman = []
    namaPengambil = []
    idGadget = []
    idpengembalian = []
    namaGadget = []
    tanggal = []
    jumlah = []
    idUser = []

    for i in range(len(index)):
        idpeminjaman.append(listReturnGadget[index[i]]['id_peminjaman'])
        idpengembalian.append(listReturnGadget[index[i]]['id'])
        tanggal.append(listReturnGadget[index[i]]['tanggal_pengembalian'])
        jumlah.append(listReturnGadget[index[i]]['jumlah_peminjaman'])

    for i in range(len(idpeminjaman)):
        for j in range(1, len(listBorrowGadget)):
            if idpeminjaman[i] == listBorrowGadget[j]['id']:
                idGadget.append(listBorrowGadget[j]['id_gadget'])
                idUser.append(listBorrowGadget[j]['id_peminjam'])

    for i in range(len(idUser)):
        for j in range(1, len(listUser)):
            if idUser[i] == listUser[j]['id']:
                namaPengambil.append(listUser[j]['nama'])
    
    for i in range(len(idGadget)):
        for j in range(1, len(listGadget)):
            if idGadget[i] == listGadget[j]['id']:
                namaGadget.append(listGadget[j]['nama'])

    listTempAll = []

    for i in range(len(idpengembalian)):
        tempAll = []
        tempAll.append(idpengembalian[i])
        tempAll.append(namaPengambil[i])
        tempAll.append(namaGadget[i])
        tempAll.append(tanggal[i])
        tempAll.append(jumlah[i])
        listTempAll.append(tempAll)

    formatReturnGadget(listTempAll)

def cariRarity(list, rarity):

    for i in range(len(list)):
        if rarity == list[i]['rarity']:
            formatGadget(GadgetCsvParser(lineParserGadget(list[i])))

def cariTahun(tahun, operator, list):

    found = False

    for i in range(1, len(list)):

        keyTahun = list[i]["tahun_ditemukan"]
        valueTahun = int(keyTahun)

        if operator == '=':
            
            if tahun == valueTahun:
                formatGadget(GadgetCsvParser(lineParserGadget(list[i])))
                found = True

        elif operator == '>':
            
            if valueTahun > tahun:
                formatGadget(GadgetCsvParser(lineParserGadget(list[i])))
                found = True

        elif operator == '>=':
            
            if valueTahun >= tahun:
                formatGadget(GadgetCsvParser(lineParserGadget(list[i])))
                found = True

        elif operator == '<':
            
            if valueTahun < tahun:
                formatGadget(GadgetCsvParser(lineParserGadget(list[i])))
                found = True

        elif operator == '<=':
            
            if valueTahun <= tahun:
                formatGadget(GadgetCsvParser(lineParserGadget(list[i])))
                found = True

    if not found:
        print("Tidak ada gadget yang ditemukan")

def tambahGadget(listGadget, id):

    listID = []

    for i in range(len(listGadget)):
        listID.append(listGadget[i]['id'])

    if id in listID:
        print("Gagal menambahkan item karena ID sudah ada")
    
    else:
        nama = input("Masukan Nama: ")
        deskripsi = input("Masukan Deskripsi: ")
        jumlah = input("Masukan Jumlah: ")
        rarity = input("Masukan rarity: ")

        listRarity = ['C', 'B', 'A', 'S']

        if rarity.upper() in listRarity:
            tahunDitemukan = input("Masukan tahun ditemukan: ")

            Dict = {

                'id' : id,
                'nama' : nama,
                'deskripsi' : deskripsi,
                'jumlah' : jumlah,
                'rarity' : rarity,
                'tahun_ditemukan' : tahunDitemukan,
            }

            listGadget.append(Dict)

            print()
            print("Item telah berhasil ditambahkan")
        
        else:
            print("Input rarity tidak valid!")

def hapusGadget(listGadget, id):

    listID = []
    found = False

    for i in range(len(listGadget)):
        listID.append(listGadget[i]['id'])

    for i in range(len(listID)):
        if id == listID[i]:
            found = True

            print(f"Apakah anda yakin ingin menghapus {listGadget[i]['nama']} (Y/N)?")
            text = input().upper()

            if text == 'Y':
                listGadget.remove(listGadget[i])
                print()
                print("Item telah berhasil dihapus dari database.")

            else:
                pass

    if not found:
        print("Tidak ada item dengan ID tersebut.")

def ubahGadget(listGadget, id):

    listID = []
    found = False

    for i in range(len(listGadget)):
        listID.append(listGadget[i]['id'])
    
    for i in range(1, len(listID)):
        if id == listID[i]:
            found = True

            Jumlah = int(input("Masukan jumlah: "))

            if Jumlah + int(listGadget[i]['jumlah']) >= 0:
                listGadget[i]['jumlah'] = str(int(listGadget[i]['jumlah']) + Jumlah)

                if Jumlah >= 0:
                    print(f"{Jumlah} {listGadget[i]['nama']} berhasil ditambahkan. Stok sekarang: {listGadget[i]['jumlah']}")
                else:
                    print(f"{Jumlah} {listGadget[i]['nama']} berhasil dibuang Stok sekarang: {listGadget[i]['jumlah']}")

                break

            else:
                print(f"{-Jumlah} {listGadget[i]['nama']} gagal dibuang karena stok kurang. Stok sekarang: {listGadget[i]['jumlah']} (< {-Jumlah})")
    
    if not found:
        print("Tidak ada item dengan ID tersebut.")

def pinjamGadget(listGadget, listPinjamGadget, id, idUser):

    listID = []
    found = False
    flag = False
    idPinjam = str(len(listPinjamGadget))
    isPinjam = "False"
    canContinue = False
    isReturned = ''

    for i in range(len(listGadget)):
        listID.append(listGadget[i]['id'])

    for i in range(len(listPinjamGadget)):
        if id == listPinjamGadget[i]['id_gadget']:
            for j in range(len(listPinjamGadget)):
                if idUser == listPinjamGadget[j]['id_peminjam']:
                    flag = True
                    if 'False' == listPinjamGadget[j]['is_returned']:
                        isReturned = False
                    elif 'True' == listPinjamGadget[j]['is_returned']:
                        isReturned = True
                        break

            if isReturned:
                canContinue = True
            elif not isReturned:
                canContinue = False
            elif isReturned == "":
                canContinue = True
        
            break
        
    if not flag:
        canContinue = True

    if canContinue:

        for i in range(1, len(listID)):
            if id == listID[i]:
                found = True

                tanggal = input("Tanggal peminjaman: ")
                Jumlah = int(input("Jumlah peminjaman: "))

                if Jumlah > int(listGadget[i]['jumlah']):
                    print("Stok barang yang dipinjam kurang! ")
                    break
                else:
                    listGadget[i]['jumlah'] = str(int(listGadget[i]['jumlah']) - Jumlah)

                    print() 
                    print(f"Item {listGadget[i]['nama']} (x{Jumlah}) berhasil dipinjam!")
                
                dict = {
                    'id' : idPinjam,
                    'id_peminjam' : idUser,
                    'id_gadget' : id,
                    'tanggal_peminjaman' : tanggal,
                    'jumlah' : str(Jumlah),
                    'is_returned' : isPinjam
                }

                listPinjamGadget.append(dict)

        if not found:
            print("Tidak ada item dengan ID tersebut.")

    else:
        print("Tidak bisa meminjam, kemabalikan dulu barang-nya!")

def returnIndexGadget(listGadget, id):

    for i in range(len(listGadget)):
        if id == listGadget[i]['id']:
            return i

def returnIndexGadgetBorrow(list, id, idUser):
    
    for i in range(len(list)):
        if id == list[i]['id_gadget']:
            if idUser == list[i]['id_peminjam']:
                return i

def returnIDGadget(list, idUser):
    
    idGadget = []
    listId = []

    for i in range(len(list)):
        if idUser == list[i]['id_peminjam']:
            if 'False' == list[i]['is_returned']:
                idGadget.append(list[i]['id_gadget'])
                listId.append(i)
    
    return (idGadget, listId)

def returnIndexBorrowGadgetDate(listBorrowGadget):
    
    tempDate = []
    tempIndex = []

    for i in range(1, len(listBorrowGadget)):
        tempDate.append(listBorrowGadget[i]['tanggal_peminjaman'])
    
    sortDateTimeGadget(tempDate)

    for i in range(len(tempDate)):
        for j in range(1, len(listBorrowGadget)):
            if tempDate[i] == listBorrowGadget[j]['tanggal_peminjaman']:
                tempIndex.append(j)

    newTempIndex = []

    for item in tempIndex:
        if item in newTempIndex:
            pass
        else:
            newTempIndex.append(item)

    return newTempIndex

def returnIndexReturnGadgetDate(listReturnGadget):
    
    tempDate = []
    tempIndex = []

    for i in range(1, len(listReturnGadget)):
        tempDate.append(listReturnGadget[i]['tanggal_pengembalian'])
    
    sortDateTimeGadget(tempDate)

    for i in range(len(tempDate)):
        for j in range(1, len(listReturnGadget)):
            if tempDate[i] == listReturnGadget[j]['tanggal_pengembalian']:
                tempIndex.append(j)

    newTempIndex = []

    for item in tempIndex:
        if item in newTempIndex:
            pass
        else:
            newTempIndex.append(item)

    return newTempIndex

def mengembalikanGadget(listGadget, listBorrowGadget, listReturnGadget, idUser):

    temp = returnIDGadget(listBorrowGadget, idUser)
    idGadget = temp[0]
    listIndexBorrowGadget = temp[1]
    listIndexGadget = []
    listNomor = []
        
    for i in range(len(idGadget)):
        index = returnIndexGadget(listGadget, idGadget[i])
        listIndexGadget.append(index)
        listNomor.append(i+1)
        print(f"{i+1}. {listGadget[index]['nama']}")

    if len(listIndexGadget) == 0:
        print("Tidak ada barang yang dipinjam")

    else:
        print()
        nomorPinjam = int(input("Masukan nomor peminjaman: "))
        if nomorPinjam in listNomor:
            jumlahSementara = listBorrowGadget[int(listIndexBorrowGadget[nomorPinjam - 1])]['jumlah']
            tanggalPengembalian = input("Tanggal pengembalian: ")
            jumlahPengembalian = int(input("Masukan jumlah pengembalian: "))


            if jumlahPengembalian <= int(jumlahSementara):
                listGadget[int(listIndexGadget[nomorPinjam - 1])]['jumlah'] = str(int(listGadget[int(listIndexGadget[nomorPinjam - 1])]['jumlah']) + jumlahPengembalian)
                listBorrowGadget[listIndexBorrowGadget[nomorPinjam - 1]]['jumlah'] = str(int(listBorrowGadget[listIndexBorrowGadget[nomorPinjam - 1]]['jumlah']) - jumlahPengembalian)

                if int(jumlahSementara) - jumlahPengembalian == 0:
                    listBorrowGadget[listIndexBorrowGadget[nomorPinjam - 1]]['is_returned'] = 'True'

                id = len(listReturnGadget)
                idPeminjaman = listBorrowGadget[int(listIndexBorrowGadget[nomorPinjam - 1])]['id']

                print()
                print(f"Item {listGadget[listIndexGadget[nomorPinjam - 1]]['nama']} (x{jumlahPengembalian}) telah dikembalikan")

                tempDict = {
                    'id' : str(id),
                    'id_peminjaman' : idPeminjaman,
                    'tanggal_pengembalian' : tanggalPengembalian,
                    'jumlah_peminjaman' : str(jumlahPengembalian)
                }
                
                listReturnGadget.append(tempDict)

            else:
                print("Kembalikan item sesuai jumlahnya!")
        else:
            print("Nomor tidak ada")


