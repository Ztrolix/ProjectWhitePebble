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

def download_files():
    print("Downloading...")

    installer_url = 'https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/WhitePebble-v5.0.0-Installer.exe.zip'

    try:
        print(f"Downloading White-Pebble v5.0.0...")
        with requests.get(installer_url, stream=True) as response:
            with open("WhitePebble-v5.0.0-Installer.exe.zip", 'wb') as f:
                total_size = int(response.headers.get('content-length', 0))
                with tqdm(total=total_size, unit='B', unit_scale=True, unit_divisor=1024) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
                        pbar.update(len(chunk))
        mark_as_installed()
        print("Download complete!")
    except Exception as e:
        print("An error occurred while downloading the installer:", e)
        mark_as_not_installed()
        
    sys.stdout = sys.__stdout__
    
def extract_modpack():
    print("Extracting...")
        
    try:
        with ZipFile("WhitePebble-v5.0.0-Installer.exe.zip", 'r') as zObject:
            destination = Path("C:/White-Pebble/")
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

def install_files():
    
    print("Installing White-Pebble v5.0.0...")
    os.system("installer-5.0.0-run.bat")
    print("Installation complete!")
    
    sys.stdout = sys.__stdout__

def create_ui_run():
    root = tk.Tk()
    root.geometry("400x300")
    root.minsize(400, 300)
    root.title("White Pebble Installer - v5.0.0")
    
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
            os.system("installer-5.0.0.bat")
            download_files()
            extract_modpack()
            install_files()
            print("Process completed successfully!")
            log_entry = "\nProcess completed successfully!\n"
            time.sleep(3)
            clearConsole()
            os.system("install-done.vbs")
            sys.exit()
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