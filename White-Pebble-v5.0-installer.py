import os
import requests
import urllib.request
from zipfile import ZipFile
from pathlib import Path
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
import logging
import sys
import time

logging.basicConfig(filename="installer_log_5.0.txt", level=logging.INFO,
                    format="%(asctime)s [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

# Create a custom StreamHandler to log console output to the log file and UI
class ConsoleLogHandler(logging.StreamHandler):
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        log_entry = self.format(record)
        self.text_widget.insert(tk.END, log_entry + "\n")
        self.text_widget.see(tk.END)

# Add the custom StreamHandler to the logger
console_handler = ConsoleLogHandler(None)
console_handler.setLevel(logging.INFO)
logging.getLogger('').addHandler(console_handler)

def clearConsole() :
    os.system('cls' if os.name == 'nt' else 'clear')

def mark_as_installed():
    with open("5.0.txt", "w") as f:
        f.write("True")

def mark_as_not_installed():
    with open("5.0.txt", "w") as f:
        f.write("False")

def get_forge_version():
    print("What version of Forge do you want?")
    print("1.12.2-14.23.5.2859")
    return "1.12.2-14.23.5.2859"  # Change this line based on user input if needed

def download_files(forge_version):
    print("Downloading...")

    forge_url = f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-installer.jar"
    forge_url2 = f"https://files.minecraftforge.net/maven/net/minecraftforge/forge/{forge_version}/forge-{forge_version}-universal.jar"
    optifine = "https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/OptiFine_1.12.2_HD_U_G5.jar"
    optifinepack = "https://github.com/MMCInstances/OptifineInstances/releases/download/v1.12.2-1.0/1.12.2.zip"
    liteloader = "http://jenkins.liteloader.com/job/LiteLoaderInstaller%201.12.2/lastSuccessfulBuild/artifact/build/libs/liteloader-installer-1.12.2-00-SNAPSHOT.jar"
    
    modpack_url = 'https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/White-Pebble-v5.0.0.zip'

    try:
        print(f"Downloading Minecraft Forge version {forge_version} Installer...")
        with requests.get(forge_url, stream=True) as response:
            with open("forge-installer.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading Forge Installer:", e)
        mark_as_not_installed()

    try:
        print(f"Downloading Minecraft Forge version {forge_version} Universal...")
        with requests.get(forge_url2, stream=True) as response:
            with open("forge-universal.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading Forge Universal:", e)
        mark_as_not_installed()
        
    try:
        print(f"Downloading Minecraft LiteLoader version 1.12.2-SNAPSHOT Installer...")
        with requests.get(liteloader, stream=True) as response:
            with open("liteloader-installer.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()
        
    try:
        print(f"Downloading Minecraft Optifine version 1.12.2-HD-U-G5 Installer...")
        with requests.get(optifine, stream=True) as response:
            with open("optifine-installer.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()
        
    download_liteloader()
        
    try:
        print(f"Downloading Minecraft Optifine version 1.12.2-HD-U-G5-Pre1 Installer...")
        with requests.get(optifinepack, stream=True) as response:
            with open("optifinepack.zip", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()

    try:
        print(f"Downloading Minecraft Forge version {forge_version} Modpack...")
        with requests.get(modpack_url, stream=True) as response:
            with open("White-Pebble-v5.0.0.zip", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        mark_as_installed()
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading the modpack:", e)
        mark_as_not_installed()
        
    sys.stdout = sys.__stdout__
    
def download_mc():
    mcserver1122 = "https://www.mc-download.com/index.php?action=downloadfile&filename=minecraft-server-1.12.2.jar&directory=Minecraft%20Versions%20Official/Minecraft%20Server&"

def download_liteloader():
    liteloaderjdoc = "https://jenkins.liteloader.com/view/1.12.2/job/LiteLoader%201.12.2/lastSuccessfulBuild/artifact/build/libs/liteloader-1.12.2-SNAPSHOT-javadoc.jar"
    liteloadersource = "https://jenkins.liteloader.com/view/1.12.2/job/LiteLoader%201.12.2/lastSuccessfulBuild/artifact/build/libs/liteloader-1.12.2-SNAPSHOT-sources.jar"
    liteloaderstage = "https://jenkins.liteloader.com/view/1.12.2/job/LiteLoader%201.12.2/lastSuccessfulBuild/artifact/build/libs/liteloader-1.12.2-SNAPSHOT-staging.jar"
    liteloaderrelease = "https://jenkins.liteloader.com/view/1.12.2/job/LiteLoader%201.12.2/lastSuccessfulBuild/artifact/build/libs/liteloader-1.12.2-SNAPSHOT-release.jar"
    
    try:
        print(f"Downloading Minecraft liteloaderjdoc Installer...")
        with requests.get(liteloaderjdoc, stream=True) as response:
            with open("liteloaderjdoc.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()
    
    try:
        print(f"Downloading Minecraft liteloadersource Installer...")
        with requests.get(liteloadersource, stream=True) as response:
            with open("liteloadersource.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()
        
    try:
        print(f"Downloading Minecraft liteloaderstage Installer...")
        with requests.get(liteloaderstage, stream=True) as response:
            with open("liteloaderstage.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()
        
    try:
        print(f"Downloading Minecraft liteloaderrelease Installer...")
        with requests.get(liteloaderrelease, stream=True) as response:
            with open("liteloaderrelease.jar", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading LiteLoader Installer:", e)
        mark_as_not_installed()

def install_forge():
    
    print("Installing Minecraft Forge Installer Server...")
    os.system("java -jar forge-installer.jar --installServer")
    print("Installation complete!")

    print("Installing Minecraft Forge Universal Server...")
    os.system("java -jar forge-universal.jar --installServer")
    print("Installation complete!")

    print("Installing Minecraft Forge Installer...")
    os.system("java -jar forge-installer.jar")
    print("Installation complete!")
    
    print("Installing Minecraft LiteLoader Installer...")
    os.system("java -jar liteloader-installer.jar")
    print("Installation complete!")
    
    print("Installing Minecraft LiteLoader Server...")
    os.system("java -jar liteloader-installer.jar --installServer")
    print("Installation complete!")
    
    print("Installing Minecraft Optifine Installer...")
    os.system("java -jar optifine-installer.jar")
    print("Installation complete!")
    
    print("Installing Minecraft Optifine Server...")
    os.system("java -jar optifine-installer.jar --installServer")
    print("Installation complete!")
    
    extract_optifine()
    print("Installing Minecraft Optifine Installer 1.12.2-HD-U-G5-Pre1...")
    os.system("java -jar libraries\OptiFine_1.12.2_HD_U_G5_pre1.jar")
    print("Installation complete!")
    
    sys.stdout = sys.__stdout__

def extract_optifine():
    print("Extracting...")

    try:
        with ZipFile("optifinepack.zip", 'r') as zObject:
            destination = Path("C:/White-Pebble/White-Pebble-5.0/")
            destination.mkdir(parents=True, exist_ok=True)
            file_count = len(zObject.infolist())
            with tqdm(total=file_count) as pbar:
                for file_info in zObject.infolist():
                    zObject.extract(file_info, path=destination)
                    pbar.update(1)
        mark_as_installed()
    except Exception as e:
        print("An error occurred while extracting the modpack:", e)
        mark_as_not_installed()
        
    sys.stdout = sys.__stdout__ 

def extract_modpack():
    print("Extracting...")

    try:
        with ZipFile("White-Pebble-v5.0.0.zip", 'r') as zObject:
            destination = Path("C:/White-Pebble/White-Pebble-5.0/instances/White-Pebble v5.0.0")
            destination.mkdir(parents=True, exist_ok=True)
            file_count = len(zObject.infolist())
            with tqdm(total=file_count) as pbar:
                for file_info in zObject.infolist():
                    zObject.extract(file_info, path=destination)
                    pbar.update(1)
        mark_as_installed()
    except Exception as e:
        print("An error occurred while extracting the modpack:", e)
        mark_as_not_installed()
        
    sys.stdout = sys.__stdout__ 
        
def create_ui_run():
    root = tk.Tk()
    root.geometry("400x300")
    root.minsize(400, 300)
    root.title("White Pebble Installer - v5.0")
    
    def display_logs():
        with open("installer_log_5.0.txt", "r") as log_file:
            logs = log_file.read()
        log_window = tk.Toplevel(root)
        log_window.title("Installer Logs")
        log_text = tk.Text(log_window, wrap=tk.WORD, font=("Courier", 12))
        log_text.insert(tk.END, logs)
        log_text.pack(fill=tk.BOTH, expand=True)

    def run_installer():
        try:
            os.system("python-installer.bat")
            forge_version = "1.12.2-14.23.5.2859"  # Replace this with your desired Forge version or implement user input
            download_files(forge_version)
            install_forge()
            extract_modpack()
            print("Process completed successfully!")
            log_entry = "\nProcess completed successfully!\n"
            time.sleep(3)
            clearConsole()
        except Exception as e:
            logging.error(f"ERROR: There was an error in the installer: {e}")
            print(f"ERROR: There was an error in the installer: {e}")
            input("Press 'ENTER' to close.")

    run_button = tk.Button(root, text="Run Installer", command=run_installer)
    run_button.pack(pady=10)

    logs_button = tk.Button(root, text="View Logs", command=display_logs)
    logs_button.pack(pady=10)
    
    root.mainloop()
    
class StdoutRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

def main():
    create_ui_run()
    
if __name__ == "__main__":
    main()