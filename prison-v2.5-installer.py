from zipfile import ZipFile
import requests

print("Downloading...")

try:
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/Prison.v2.5.zip')
    with open("Prison v2.5.zip", 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")
    d = open("2.5.txt", "w")
    d.write("False")
    d.close()
    
print("Extracting...")

try:
	with ZipFile("Prison v2.5.zip", 'r') as zObject:

		# Extracting all the members of the zip
		# into a specific location.
		zObject.extractall(
			path="C:\\White-Pebble\\instances\\Prison v2.5")
	f = open("2.5.txt", "w")
	f.write("True")
	f.close()
except:
    print("An error occurred!")
    d = open("2.5.txt", "w")
    d.write("False")
    d.close()