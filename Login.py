from Function import *

def login():
    username = input("Masukan username: ")
    password = input("Masukan password: ")

    listUser = readUser()
    checkPassword = ''

    for i in range(len(listUser)):
                if username == listUser[i]['username']:
                    checkPassword = listUser[i]['password']

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

            if (checkPassword != password):
                print("Username atau password salah!")
                print("")

        print()
        print(f"Halo {username}! Selamat datang di Kantong Ajaib")
        print()
   