# put your name as a comment at the top of your program

# this statement lets you use the random number generator
import random

# this statement generates an integer from 0 to 100 inclusive
# and stores it in the variable secretNum
secretNum = random.randint(1,100)

print()
print("The computer has selected a secret number from 0 to 100 inclusive\n")
print("You have to guess it in as few tries as possible.\n")
print("To do this enter a number between 0 and 100 and the computer will")
print("tell you if your guess is lower or higher than the secret number.")
print("When you guess the correct number the computer will tell you")
print("you how many guesses it took.")

# your code goes here