import os
import time

install = ""

v50 = open("5.0.txt", "r")
v50r = v50.read()

while True:
    v50 = open("5.0.txt", "r")
    v50r = v50.read()
    
    print("0) Custom Install")
    if (v50r == "True") :
        print("1) White-Pebble v5.0 [Installed]")
    else :
        print("1) White-Pebble v5.0 [Not-Installed]")
    install = input(": ")
    
    if (install == "0") :
        os.system("custom-installs.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (install == "1") :
        os.system("installer-5.0.0.py")
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
    os.system("installermenu.py")