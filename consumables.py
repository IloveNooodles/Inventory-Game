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