import os
import time

v11 = open("1.1.txt", "r")
v11r = v11.read()

v21 = open("2.1.txt", "r")
v21r = v21.read()

v22 = open("2.2.txt", "r")
v22r = v22.read()

v23 = open("2.3.txt", "r")
v23r = v23.read()

v24 = open("2.4.txt", "r")
v24r = v24.read()

v25 = open("2.5.txt", "r")
v25r = v25.read()

v30 = open("3.0.txt", "r")
v30r = v30.read()

v31 = open("3.1.txt", "r")
v31r = v31.read()

v41 = open("4.1.txt", "r")
v41r = v41.read()

while True:
    v11 = open("1.1.txt", "r")
    v11r = v11.read()

    v21 = open("2.1.txt", "r")
    v21r = v21.read()

    v22 = open("2.2.txt", "r")
    v22r = v22.read()

    v23 = open("2.3.txt", "r")
    v23r = v23.read()

    v24 = open("2.4.txt", "r")
    v24r = v24.read()

    v25 = open("2.5.txt", "r")
    v25r = v25.read()
    
    v30 = open("3.0.txt", "r")
    v30r = v30.read()
    
    v31 = open("3.1.txt", "r")
    v31r = v31.read()
    
    v41 = open("4.1.txt", "r")
    v41r = v41.read()
    
    print("0) Custom Install")
    if (v11r == "True") :
        print("1) Prison v1.1 [Installed]")
    else :
        print("1) Prison v1.1 [Not-Installed]")
    if (v21r == "True") :
        print("2) Prison v2.1 [Installed]")
    else :
        print("2) Prison v2.1 [Not-Installed]")
    if (v22r == "True") :
        print("3) Prison v2.2 [Installed]")
    else :
        print("3) Prison v2.2 [Not-Installed]")
    if (v23r == "True") :
        print("4) Prison v2.3 [Installed]")
    else :
        print("4) Prison v2.3 [Not-Installed]")
    if (v24r == "True") :
        print("5) Prison v2.4 [Installed]")
    else :
        print("5) Prison v2.4 [Not-Installed]")
    if (v25r == "True") :
        print("6) Prison v2.5 [Installed]")
    else :
        print("6) Prison v2.5 [Not-Installed]")
    if (v30r == "True") :
        print("7) White-Pebble v3.0 [Installed]")
    else :
        print("7) White-Pebble v3.0 [Not-Installed]")
    if (v31r == "True") :
        print("8) White-Pebble v3.1 [Installed]")
    else :
        print("8) White-Pebble v3.1 [Not-Installed]")
    if (v41r == "True") :
        print("9) White-Pebble v4.1 [Installed]")
    else :
        print("9) White-Pebble v4.1 [Not-Installed]")
    install = input(": ")
    
    if (install == "0") :
        os.system("custom-install.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "1") :
        os.system("prison-v1.1-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "2") :
        os.system("prison-v2.1-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "3") :
        os.system("prison-v2.2-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "4") :
        os.system("prison-v2.3-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "5") :
        os.system("prison-v2.4-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "6") :
        os.system("prison-v2.5-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "7") :
        os.system("White-Pebble-v3.0-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "8") :
        os.system("White-Pebble-v3.1-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "9") :
        os.system("White-Pebble-v4.1-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else :
        print("'" + install + "' is not a valid number.")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
       
    time.sleep(1) 
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    os.system("installer.py")