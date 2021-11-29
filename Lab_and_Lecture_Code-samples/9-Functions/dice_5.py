import datetime
import random

def checkSides(sides):
    good_sides = [4,6,8,10,12,20]
    if good_sides.count(sides) != 1:
        print("error, bad side number\nusing default value of 6")
        return 6
    return sides

def dice(sides, rolls):
    sides = checkSides(sides)
    darr = []
    for c in range(rolls):
        darr.append(random.randint(1, sides))
    return darr


gorun = True
nrolls = int(input("Enter the number of dice to roll-> "))
nsides = int(input("Enter the number of sides the dice have-> "))
while(gorun):
    c = 1
    print("------------------")
    for adice in dice(nsides, nrolls):
        print(c, datetime.datetime.now(), adice )
        c += 1
    print("------------------")
    select = input("Press Enter to re-roll, q to quit, or n to set new parameters-> ")
    if select == 'q':
        break
    elif select == 'n':
        nrolls = int(input("Enter the number of dice to roll-> "))
        nsides = int(input("Enter the number of sides the dice have-> "))

print("Thank you")