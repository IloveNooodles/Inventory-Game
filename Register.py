from Function import *

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

def register():    
    listUser = readUser()
    listUsername = makeList(listUser, "username")
    filename = 'data/user.csv'

    nama = input("Masukan nama: ")
    username = input("Masukan username: ")

    while checkFunction(listUsername, username):
        print("Username sudah ada, silahkan gunakan username yang lain!")
        username = input("Masukan username: ")

    password = input("Masukan password: ")
    alamat = input("Masukan alamat: ")
    id = str(len(listUser))
    role = "user"

    # content = function.lineParser(id, username, nama, alamat, password, role)
    # function.writeFile(filename, content)

    print()
    print(f"User {username} telah berhasil register kedalam Kantong Ajaib.")
    print()