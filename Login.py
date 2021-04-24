from Function import *

def login(folder):
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    listUser = readUser(folder)
    checkPassword = ''
    idUser = ''
    roleUser = ''

    for i in range(len(listUser)):
                if username == listUser[i]['username']:
                    checkPassword = listUser[i]['password']
                    idUser = str(i)
                    roleUser = listUser[i]['role']

    if checkPassword == password:
        print()
        print(f"Halo {username}! Selamat datang di Kantong Ajaib")
        print()

    else:
        print("Username atau password salah!")
        print()
        while checkPassword != password:

            username = input("Masukan username: ")
            password = input("Masukan password: ")

            for i in range(len(listUser)):
                if username == listUser[i]['username']:
                    checkPassword = listUser[i]['password']
                    idUser = str(i)

            if (checkPassword != password):
                print("Username atau password salah!")
                print("")

        print()
        print(f"Halo {username}! Selamat datang di Kantong Ajaib")
    
    return (idUser, roleUser)
   