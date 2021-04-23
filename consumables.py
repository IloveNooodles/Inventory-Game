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