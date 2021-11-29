#pyFileIO-simpleWrite.py

f1 = open("testfile.txt", "w")

f1.write("this is a test\n")
f1.write("adding another line\n")

mytxt = input("enter some text ")
f1.write(mytxt)
print("check testfile.txt for results")

f1.close()
