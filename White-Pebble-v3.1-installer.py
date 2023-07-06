from zipfile import ZipFile
import requests

print("Downloading...")

try:
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/White-Pebble-v3.1.zip')
    with open("White-Pebble-v3.1.zip", 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")
    d = open("3.1.txt", "w")
    d.write("False")
    d.close()

print("Extracting...")

try:
	with ZipFile("White-Pebble-v3.1.zip", 'r') as zObject:

		# Extracting all the members of the zip
		# into a specific location.
		zObject.extractall(
			path="C:\\White-Pebble\\instances\\White-Pebble v3.1")
	f = open("3.1.txt", "w")
	f.write("True")
	f.close()
except:
    print("An error occurred while extracting!")
    d = open("3.1.txt", "w")
    d.write("False")
    d.close()