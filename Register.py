from Function import *

def register():    
    listUser = readUser()
    listUsername = makeList(listUser, "username")
    filename = 'data/user.csv'

    nama = input("Masukan nama: ").title()
    username = input("Masukan username: ")

    while checkFunction(listUsername, username):
        print("Username sudah ada, silahkan gunakan username yang lain!")
        username = input("Masukan username: ")

    password = input("Masukan password: ")
    alamat = input("Masukan alamat: ")
    id = str(len(listUser))
    role = "user"

    content = lineParser(id, username, nama, alamat, password, role)
    writeFile(filename, content)

    print()
    print(f"User {username} telah berhasil register kedalam Kantong Ajaib.")
    print()