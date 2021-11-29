import random

def myThing():
    print("thing")

def printHappy(var1, blob):
    print(var1 * blob)

def myAdd(var1, var2):
    c = var1 + var2
    return c

def printStar(num):
    print("*" * num)

# --------------------------

print(random.random())

printHappy("happy", 4)
printHappy("joy", 6)

sum = myAdd(4, 77)
print(sum)

printStar(20)
print("all done")

