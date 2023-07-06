from zipfile import ZipFile
import requests

web = input("Zip File: ")
name = input("Zip Name (DO NOT ADD '.zip' AT THE END): ")
name2 = name + ".zip"

print("Downloading...")

try:
    response = requests.get(str(web))
    with open(name2, 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")

print("Extracting...")

try:
	with ZipFile(name2, 'r') as zObject:

		# Extracting all the members of the zip
		# into a specific location.
		zObject.extractall(
			path="C:\\White-Pebble\\instances\\" + name)
except:
    print("An error occurred while extracting!")