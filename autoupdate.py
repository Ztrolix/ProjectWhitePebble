import os
import requests

print("Downloading...")

try:
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/AUTOUPDATE/autoupdate2.py')
    with open("autoupdate2.py", 'wb') as f:
        f.write(response.content)
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/AUTOUPDATE/AutoUpdateWhitePebble.exe')
    with open("autoupdate.exe", 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")

os.system("autoupdate2.py")