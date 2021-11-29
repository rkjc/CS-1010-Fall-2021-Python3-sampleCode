 

import random

secretNum = random.randint(1,10)
count = 0

#print(secretNum)

userNum = int(input("guess a number > "))
count += 1
if userNum > secretNum:
    print("greater")
if userNum < secretNum:
    print("less")
if userNum == secretNum:
    print("WooHoo you got it")
    print("you made", count, "guesses")
else:
    userNum = int(input("guess a number > "))
    count += 1
    if userNum > secretNum:
        print("greater")
    if userNum < secretNum:
        print("less")
    if userNum == secretNum:
        print("WooHoo you got it")
        print("count is ", count)
    else:
        userNum = int(input("guess a number > "))
        count += 1
        if userNum > secretNum:
            print("greater")
        if userNum < secretNum:
            print("less")
        if userNum == secretNum:
            print("WooHoo you got it")
            print("count is ", count)
        else:
            userNum = int(input("guess a number > "))
            count += 1
            if userNum > secretNum:
                print("greater")
            if userNum < secretNum:
                print("less")
            if userNum == secretNum:
                print("WooHoo you got it")
                print("count is ", count)
            else:
                userNum = int(input("guess a number > "))
                count += 1
                if userNum > secretNum:
                    print("greater")
                if userNum < secretNum:
                    print("less")
                if userNum == secretNum:
                    print("WooHoo you got it")
                    print("count is ", count)
                else:
                   print("sorry you did not get it. The number was", secretNum)
