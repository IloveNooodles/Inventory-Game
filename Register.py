from Function import *

def register(listUser):    
    
    listUsername = makeList(listUser, "username")

    nama = input("Masukan nama: ").title()
    username = input("Masukan username: ")

    while checkFunction(listUsername, username):

        print()
        print("Username sudah ada, silahkan gunakan username yang lain!")
        username = input("Masukan username: ")

    password = input("Masukan password: ")
    alamat = input("Masukan alamat: ")
    id = str(len(listUser))
    role = "user"

    tempDict = {
        'id' : id,
        'username' : username,
        'nama' : nama,
        'alamat' : alamat,
        'password' : password,
        'role' : role
    }

    print()
    print(f"User {username} telah berhasil register kedalam Kantong Ajaib.")

    listUser.append(tempDict)
    return listUser

    # content = lineParser(id, username, nama, alamat, password, role)
    # appendFile(filename, content)