 
import random
import sys

scrtNum = random.randint(1,20)
num_of_guesses = 1

print()
print("The computer has selected a secret number from 0 to 20 inclusive\n")
print("You have to guess it in as few tries as possible.\n")
print("To do this enter a number between 0 and 20 and the computer will")
print("tell you if your guess is lower or higher than the secret number.")
print("When you guess the correct number the computer will tell you")
print("you how many guesses it took.")

print("-----------------------------------")

myguess = int(input("Enter your guess -> "))       
if myguess == scrtNum:
    print("you win. It took this many guesses ", num_of_guesses)
    input("press enter to exit")
    sys.exit(0)
else:
    if myguess < scrtNum:
        print("Lower")
        num_of_guesses += 1
    else:
        print("Higher")
        num_of_guesses += 1

myguess = int(input("Enter your guess -> "))       
if myguess == scrtNum:
    print("you win. It took this many guesses ", num_of_guesses)
    input("press enter to exit")
    sys.exit(0)
else:
    if myguess < scrtNum:
        print("Lower")
        num_of_guesses += 1
    else:
        print("Higher")
        num_of_guesses += 1
        
myguess = int(input("Enter your guess -> "))       
if myguess == scrtNum:
    print("you win. It took this many guesses ", num_of_guesses)
    input("press enter to exit")
    sys.exit(0)
else:
    if myguess < scrtNum:
        print("Lower")
        num_of_guesses += 1
    else:
        print("Higher")
        num_of_guesses += 1
        
myguess = int(input("Enter your guess -> "))       
if myguess == scrtNum:
    print("you win. It took this many guesses ", num_of_guesses)
    input("press enter to exit")
    sys.exit(0)
else:
    if myguess < scrtNum:
        print("Lower")
        num_of_guesses += 1
    else:
        print("Higher")
        num_of_guesses += 1
        

print("Sorry, you missed it. It took this many guesses ", num_of_guesses)

input("press enter to exit")
