from Function import *

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

def cariRarity(list, rarity):

    for i in range(len(list)):
        if rarity == list[i]['rarity']:
            formatGadget(CSVParser(lineParser(list[i])))

def cariTahun(tahun, operator, list):

    found = False

    for i in range(len(list)):

        keyTahun = list[i]["tahun_ditemukan"]
        valueTahun = int(keyTahun)

        if operator == '=':
            
            if tahun == valueTahun:
                formatGadget(CSVParser(lineParser(list[i])))
                found = True

        elif operator == '>':
            
            if valueTahun > tahun:
                formatGadget(CSVParser(lineParser(list[i])))
                found = True

        elif operator == '>=':
            
            if valueTahun >= tahun:
                formatGadget(CSVParser(lineParser(list[i])))
                found = True

        elif operator == '<':
            
            if valueTahun < tahun:
                formatGadget(CSVParser(lineParser(list[i])))
                found = True

        elif operator == '<=':
            
            if valueTahun <= tahun:
                formatGadget(CSVParser(lineParser(list[i])))
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
    idPinjam = str(len(listPinjamGadget))
    isPinjam = "False"

    for i in range(len(listGadget)):
        listID.append(listGadget[i]['id'])
    
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

# def mengembalikanGadget(listGadget, ):

    
