from zipfile import ZipFile
import requests

print("Downloading...")

try:
    response = requests.get('https://github.com/Ztrolix/ProjectWhitePebble/releases/download/versions/Prison.v1.1.zip')
    with open("Prison v1.1.zip", 'wb') as f:
        f.write(response.content)
except:
    print("An error occurred while downloading!")
    d = open("1.1.txt", "w")
    d.write("False")
    d.close()
    
print("Extracting...")

try:
	with ZipFile("Prison v1.1.zip", 'r') as zObject:

		# Extracting all the members of the zip
		# into a specific location.
		zObject.extractall(
			path="C:\\White-Pebble\\instances\\Prison v1.1")
	f = open("1.1.txt", "w")
	f.write("True")
	f.close()
except:
    print("An error occurred!")
    d = open("1.1.txt", "w")
    d.write("False")
    d.close()