# EX3-Function-lab.py
# Richard Cross - 2021-10-26
# import statements
import random

# function definitions
def checkSides(sides):
    if not ([4, 6, 8, 10, 12, 20].count(sides) == 1):
        print("* Error *\n  Invalid number of sides.\n  Valid sides are: 4,6,8,12,20\n  Using default of 6 sides.")
        return False
    else:
        return True

def dice_5(sides, rolls):
    if not(checkSides(sides)):
        sides=6
    resultArr = []
    for x in range(rolls):
        rndNum = random.randint(1, sides)
        resultArr.append(rndNum)
    return resultArr

def matchLine(theArr):
    retStr = "----"
    for d in theArr:
        if d < 10:
            retStr += "-----"
        else:
            retStr += "------"
    return retStr

# main body of code

r = int(input("Enter the number of dice to roll-> "))
s = int(input("Enter the number of sides the dice have-> "))
diceRolls = dice_5(s,r)

print(matchLine(diceRolls))
print()

print("    ", end="")
for dice in diceRolls:
    print(dice, end="    ")
print()

print()
print(matchLine(diceRolls))


#parameters