# User has to guess secret number
# this statement lets you use the random number generator
import random

# this statement generates an integer from 0 to 10 inclusive
# and stores it in the variable secretNum
secretNum = random.randint(1,10)
#print(secretNum)

print()
print("The computer has selected a secret number from 0 to 10 inclusive\n")
print("You have to guess it in as few tries as possible.\n")
print("To do this enter a number between 0 and 100 and the computer will")
print("tell you if your guess is lower or higher than the secret number.")
print("When you guess the correct number the computer will tell you")
print("you how many guesses it took.")

count = 0

userGuess = int(input("Enter a guess for the secret number > "))
count += 1
if userGuess > secretNum:
    print("guess is higher than secret number")
if userGuess < secretNum:
    print("guess is lower than secret number")
if userGuess == secretNum:
    print("GREAT you won")
    print("num of guesses", count)
    exit()

userGuess = int(input("Enter a guess for the secret number > "))
count += 1
if userGuess > secretNum:
    print("guess is higher than secret number")
if userGuess < secretNum:
    print("guess is lower than secret number")
if userGuess == secretNum:
    print("GREAT you won")
    print("num of guesses", count)
    exit()

userGuess = int(input("Enter a guess for the secret number > "))
count += 1
if userGuess > secretNum:
    print("guess is higher than secret number")
if userGuess < secretNum:
    print("guess is lower than secret number")
if userGuess == secretNum:
    print("GREAT you won")
    print("num of guesses", count)
    exit()

userGuess = int(input("Enter a guess for the secret number > "))
count += 1
if userGuess > secretNum:
    print("guess is higher than secret number")
if userGuess < secretNum:
    print("guess is lower than secret number")
if userGuess == secretNum:
    print("GREAT you won")
    print("num of guesses", count)
    exit()

print(count, "guesses and you didn't make it, number was", secretNum )