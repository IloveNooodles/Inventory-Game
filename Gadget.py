from Function import *

def formatGadget(list):

    nama = list[1]
    deskripsi = list[2]
    jumlah = list[3]
    rarity = list[4]
    tahunDitemukan = list[5]

    print(f"Nama\t\t: {nama}")
    print(f"Deskripsi\t: {deskripsi}")
    print(f"Jumlah\t\t: {jumlah}")
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