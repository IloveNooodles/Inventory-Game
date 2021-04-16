def readFile(filename):
    with open (filename, 'r') as file:
        contents = file.read()

def writeFile(filename, text):
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

def makeCsv(): #membuat csv dari fucntion
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
        file.write("id;id_pengambil;id_consumable;tanggal_peminjaman;jumlah")

def CSVParser(lines): #Memparse CSV ke dalam bentuk list
    listReturn = []
    text = ''

    for char in lines:
        if char == ';' or char == '\n':
            listReturn.append(text)
            text = ''
        elif char == lines[-1]:
            text += char
            listReturn.append(text)
        else:
            text += char

    return listReturn

def lineParser(*args):
    text = ''

    for arg in args:
        text += (arg)
        if arg:
            text += ';'
    text = text[:-1]   

    return text

def makeList (list, keyword):
    newList = []

    for i in range(len(list)):
        newList.append(list[i][keyword])
    
    return newList

def readUser():
    user = []

    filename = "data/user.csv"
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