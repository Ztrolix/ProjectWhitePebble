import os
import time

v12012 = open("1.20.1.2.txt", "r")
v12012r = v12012.read()

while True:
    v12012 = open("1.20.1.2.txt", "r")
    v12012r = v12012.read()
    
    print("0) Custom Install")
    if (v12012r == "True") :
        print("1) White-Pebble Bedrock 1.20.1.2 [Installed]")
    else :
        print("1) White-Pebble Bedrock 1.20.1.2 [Not-Installed]")
        
    bedinstall = input(": ")
        
    if (bedinstall == "0") :
        os.system("custom-bedrock.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    elif (bedinstall == "1") :
        os.system("bedrock-1.20.1.2-installer.py")
        print("Done!")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else :
        print("'" + bedinstall + "' is not a valid number.")
        print()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
       
    time.sleep(1) 
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    os.system("bedrockinstalls.py")