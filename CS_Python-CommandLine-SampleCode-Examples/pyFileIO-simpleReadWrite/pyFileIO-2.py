myfile = open("newtestfile1.txt", "w")
print("write your story")
words = ""

while(words != "end"):
  words = input()
  myfile.write(words)
  myfile.write("\n")

myfile.close()

