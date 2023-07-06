from zipfile import ZipFile
import requests

print("Downloading...")

try:
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/bedrock-1.12.1.2.zip')
    with open("bedrock-1.12.1.2.zip", 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")
    d = open("1.20.1.2.txt", "w")
    d.write("False")
    d.close()

print("Extracting...")

try:
	with ZipFile("bedrock-1.12.1.2.zip", 'r') as zObject:

		# Extracting all the members of the zip
		# into a specific location.
		zObject.extractall(
			path="C:\\White-Pebble\\.minecraft_bedrock\\versions")
	f = open("1.20.1.2.txt", "w")
	f.write("True")
	f.close()
except:
    print("An error occurred while extracting!")
    d = open("1.20.1.2.txt", "w")
    d.write("False")
    d.close()