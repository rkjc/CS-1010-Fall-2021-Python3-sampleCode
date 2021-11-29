#pyFileIO-simpleRead.py

myfile = open("testfile.txt", "r")
textFileContent = myfile.read()

print("- file contents are -\n")
print(textFileContent)

myfile.close()
