
import random


secretNum = random.randint(1,10)
count = 0

def doThis():
    userNum = int(input("guess a number > "))
    count += 1
    if userNum > secretNum:
        print("greater")
    if userNum < secretNum:
        print("less")
    if userNum == secretNum:
        print("WooHoo you got it")
        print("you made", count, "guesses")
        exit()

userNum = int(input("guess a number > "))
count += 1
if userNum > secretNum:
    print("greater")
if userNum < secretNum:
    print("less")
if userNum == secretNum:
    print("WooHoo you got it")
    print("count is ", count)
    exit()

userNum = int(input("guess a number > "))
count += 1
if userNum > secretNum:
    print("greater")
if userNum < secretNum:
    print("less")
if userNum == secretNum:
    print("WooHoo you got it")
    print("count is ", count)
    exit()

userNum = int(input("guess a number > "))
count += 1
if userNum > secretNum:
    print("greater")
if userNum < secretNum:
    print("less")
if userNum == secretNum:
    print("WooHoo you got it")
    print("count is ", count)
    exit()

userNum = int(input("guess a number > "))
count += 1
if userNum > secretNum:
    print("greater")
if userNum < secretNum:
    print("less")
if userNum == secretNum:
    print("WooHoo you got it")
    print("count is ", count)
    exit()

print("sorry you did not get it. The number was", secretNum)