import datetime

def tambahConsumables(list, id):

    listID = []

    for i in range(len(list)):
        listID.append(list[i]['id'])

    if id in listID:
        print("Gagal menambahkan item karena ID sudah ada")
    
    else:
        nama = input("Masukan Nama: ")
        deskripsi = input("Masukan Deskripsi: ")
        jumlah = input("Masukan Jumlah: ")
        rarity = input("Masukan rarity: ")

        listRarity = ['C', 'B', 'A', 'S']

        if rarity.upper() in listRarity:
            
            Dict = {
                'id' : id,
                'nama' : nama,
                'deskripsi' : deskripsi,
                'jumlah' : jumlah,
                'rarity' : rarity,
            }

            list.append(Dict)

            print()
            print("Item telah berhasil ditambahkan")
        
        else:
            print("Input rarity tidak valid!")

def hapusConsumables(listConsumables, id):

    listID = []
    found = False

    for i in range(len(listConsumables)):
        listID.append(listConsumables[i]['id'])

    for i in range(len(listID)):
        if id == listID[i]:
            found = True
            print(f"Apakah anda yakin ingin menghapus {listConsumables[i]['nama']} (Y/N)?")
            text = input().upper()

            if text == 'Y':
                listConsumables.remove(listConsumables[i])
                print(listConsumables)
                print()
                print("Item telah berhasil dihapus dari database.")
            else:
                pass
    
    if not found:
        print("Tidak ada item dengan ID tersebut.")

def ubahConsumables(listConsumables, id):

    listID = []
    found = False

    for i in range(len(listConsumables)):
        listID.append(listConsumables[i]['id'])
    
    for i in range(1, len(listID)):
        if id == listID[i]:
            found = True

            Jumlah = int(input("Masukan jumlah: "))

            if Jumlah + int(listConsumables[i]['jumlah']) >= 0:
                listConsumables[i]['jumlah'] = str(int(listConsumables[i]['jumlah']) + Jumlah)

                if Jumlah >= 0:
                    print(f"{Jumlah} {listConsumables[i]['nama']} berhasil ditambahkan. Stok sekarang: {listConsumables[i]['jumlah']}")
                else:
                    print(f"{Jumlah} {listConsumables[i]['nama']} berhasil dibuang Stok sekarang: {listConsumables[i]['jumlah']}")

                break

            else:
                print(f"{-Jumlah} {listConsumables[i]['nama']} gagal dibuang karena stok kurang. Stok sekarang: {listConsumables[i]['jumlah']} (< {-Jumlah})")
    
    if not found:
        print("Tidak ada item dengan ID tersebut.")

def memintaConsumables(listConsumables, listConsumableReturn, id, idUser):

    listId = []
    found = False

    for i in range(len(listConsumables)):
        listId.append(listConsumables[i]['id'])
    
    for i in range(len(listId)):
        if id == listId[i]:
            found = True

            jumlah = int(input("Jumlah: "))

            if jumlah > int(listConsumables[i]['jumlah']):
                print("Gagal diambil karena stok kurang!")
            
            else:
                tanggalPermintaan = input("Tanggal permintaan: ")
                print(f"Item {listConsumables[i]['nama']} (x{jumlah}) telah berhasil diambil!")

                listConsumables[i]['jumlah'] = str(int(listConsumables[i]['jumlah']) - jumlah)

                newId = str(len(listConsumableReturn))

                dict = {
                    'id' : newId,
                    'id_pengambil' : idUser,
                    'id_consumable' : id,
                    'tanggal_peminjaman' : tanggalPermintaan,
                    'jumlah' : str(jumlah)
                }

                listConsumableReturn.append(dict)

    if not found:
        print("Tidak ada item dengan ID tersebut.")

def sortDateTimeConsumables(list):
    list.sort(key = lambda date : datetime.datetime.strptime(date, "%d/%m/%Y"), reverse = True)
    return list

def returnIndexAmbilConsumablesDate(listConsumablesHistory):
    
    tempDate = []
    tempIndex = []

    for i in range(1, len(listConsumablesHistory)):
        tempDate.append(listConsumablesHistory[i]['tanggal_pengambilan'])
    
    sortDateTimeConsumables(tempDate)

    for i in range(len(tempDate)):
        for j in range(1, len(listConsumablesHistory)):
            if tempDate[i] == listConsumablesHistory[j]['tanggal_pengambilan']:
                tempIndex.append(j)

    newTempIndex = []

    for item in tempIndex:
        if item in newTempIndex:
            pass
        else:
            newTempIndex.append(item)

    return newTempIndex

def formatReturnConsumables(list):
    
    counter = 0

    for i in range(len(list)):

        counter += 1

        idpengambil = list[i][0]
        namaPengambil = list[i][1]
        namaConsumable = list[i][2]
        tanggalPengembalian = list[i][3]
        Jumlah = str(list[i][4])

        print(f"ID Pengambilan\t\t: {idpengambil}")
        print(f"Nama Pengambil\t\t: {namaPengambil}")
        print(f"Nama Consumable\t\t: {namaConsumable}")
        print(f"Tanggal Pengembalian\t: {tanggalPengembalian}")
        print(f"Jumlah\t\t\t: {Jumlah}")
        print()

        if i == len(list):
            break

        if counter%5 == 0:
            text = input("Apakah ingin dilanjutkan (Y/N)? ").upper()
            if text == 'N':
                break

            print()

def RiwayatAmbilConsumables(listConsumableHistory, listUser, listConsumable):
    
    index = returnIndexAmbilConsumablesDate(listConsumableHistory)

    idpengambil = []
    idConsumable = []
    idambil = []
    namaConsumables = []
    tanggal = []
    jumlah = []
    namaPengambil = []

    for i in range(len(index)):
        idpengambil.append(listConsumableHistory[index[i]]['id_pengambil'])
        idConsumable.append(listConsumableHistory[index[i]]['id_consumable'])
        idambil.append(listConsumableHistory[index[i]]['id'])
        tanggal.append(listConsumableHistory[index[i]]['tanggal_pengambilan'])
        jumlah.append(listConsumableHistory[index[i]]['jumlah'])
    
    for i in range(len(idpengambil)):
        for j in range(1, len(listUser)):
            if idpengambil[i] == listUser[j]['id']:
                namaPengambil.append(listUser[j]['nama'])
    
    for i in range(len(idConsumable)):
        for j in range(1, len(listConsumable)):
            if idConsumable[i] == listConsumable[j]['id']:
                namaConsumables.append(listConsumable[j]['nama'])

    listTempAll = []

    for i in range(len(idambil)):
        tempAll = []
        tempAll.append(idambil[i])
        tempAll.append(namaPengambil[i])
        tempAll.append(namaConsumables[i])
        tempAll.append(tanggal[i])
        tempAll.append(jumlah[i])
        listTempAll.append(tempAll)

    formatReturnConsumables(listTempAll)
