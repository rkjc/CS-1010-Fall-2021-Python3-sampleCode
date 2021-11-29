# Richard Cross
# EX2 Functions Lab S2021
import random

#1
def dice_1():
    diceNum = random.randint(1, 6)
    return diceNum

#2
def dice_2(sides):
    diceNum = random.randint(1, sides)
    return diceNum

#3
def dice_3(sides=6):
    diceNum = random.randint(1, sides)
    return diceNum

#4

def checkSides(sides):
    if not ([4, 6, 8, 10, 12, 20].count(sides) == 1):
        print("* Error *\n  Invalid number of sides.\n  Valid sides are: 4,6,8,12,20\n  Using default of 6 sides.")
        return False
    else:
        return True

def dice_4(sides=6):
    if not(checkSides(sides)):
        sides=6
    diceNum = random.randint(1, sides)
    return diceNum

#5
def dice_5(sides, rolls):
    if not(checkSides(sides)):
        sides=6
    resultArr = []
    for x in range(rolls):
        rndNum = random.randint(1, sides)
        resultArr.append(rndNum)
    return resultArr

# -----------------


print("dice_1() -> ", dice_1())

print("dice_2(9) -> ", dice_2(9))

# check dice_3(sides) with a parameter to see it work
print("dice_3(2) -> ", dice_3(2))
# check dice_3() with no parameters to see if it still works
print("dice_3() -> ", dice_3())

# check dice_4() with an invalid
print("dice_4(3000) -> ", dice_4(3000))
print("dice_4() -> ", dice_4())
# check dice_4(sides) with a valid parameters
print("dice_4(8) -> ", dice_4(8))

print("dice_5 -> ", dice_5(6, 5))
