f1 = open("testfile.txt", "w")

f1.write("this is a test\n")
f1.write("adding another line")

num = input("enter num")
print(type(num))
print("all done")

f1.close()