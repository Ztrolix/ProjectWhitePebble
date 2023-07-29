from zipfile import ZipFile
import requests
import os
import urllib.request
import zipfile
import subprocess
import time

def version():
    print("What version of Forge do you want?")
    print("1.12.2-14.23.5.2859")
    return "1.12.2-14.23.5.2859"  # Change this line based on user input if needed

def download(forge_version):
    print("Downloading...")

    forge_url = f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-installer.jar"
    forge_url2 = f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-universal.jar"
    
    print(f"Downloading Minecraft Forge version {forge_version} Installer...")
    urllib.request.urlretrieve(forge_url, "forge-installer.jar")
    print("Download complete!")

    print(f"Downloading Minecraft Forge version {forge_version} Universal...")
    urllib.request.urlretrieve(forge_url2, "forge-universal.jar")
    print("Download complete!")

    try:
        print(f"Downloading Minecraft Forge version {forge_version} Modpack...")
        response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/White-Pebble-v4.4.1.zip')
        with open("White-Pebble-v4.4.1.zip", 'wb') as f:
            f.write(response.content)
    except:
        print("An error occurred while downloading!")
        d = open("4.4.1.txt", "w")
        d.write("False")
        d.close()

def install():
    print("Installing Minecraft Forge Installer Server...")
    os.system("java -jar forge-installer.jar --installServer")
    print("Installation complete!")

    print("Installing Minecraft Forge Universal Server...")
    os.system("java -jar forge-universal.jar --installServer")
    print("Installation complete!")

    print("Installing Minecraft Forge Installer...")
    os.system("java -jar forge-installer.jar")
    print("Installation complete!")

def extract():

    print("Extracting...")

    try:
    	with ZipFile("White-Pebble-v4.4.1.zip", 'r') as zObject:

    		# Extracting all the members of the zip
    		# into a specific location.
    		zObject.extractall(
    			path="C:\\White-Pebble\\instances\\White-Pebble v4.4.1")
    	f = open("4.4.1.txt", "w")
    	f.write("True")
    	f.close()
    except:
        print("An error occurred while extracting!")
        d = open("4.4.1.txt", "w")
        d.write("False")
        d.close()

def main():

    try:
        forge_version = version()
    except Exception as e:
        print(f"ERROR: There was an error in 'version()': {e}")
        input("Press 'ENTER' to close.")

    try:
        download(forge_version)
    except Exception as e:
        print(f"ERROR: There was an error in 'download()': {e}")
        input("Press 'ENTER' to close.")
    
    try:
        install()
    except Exception as e:
        print(f"ERROR: There was an error in 'install()': {e}")
        input("Press 'ENTER' to close.")
    
    try:
        extract()
    except Exception as e:
        print(f"ERROR: There was an error in 'extract()': {e}")
        input("Press 'ENTER' to close.")

if __name__ == "__main__":
    main()