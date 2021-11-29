import random
snum = random.randint(1,10)
count = 0

# make a function that can respond to a guess
def doThis():
    global count
    global snum
    global guess
    guess = int(input("Try to guess the secret number > "))
    count += 1
    if guess < snum:
        print("Your guess was less than the secret number.")
    elif guess > snum:
        print("Your guess was greater than the secret number.")
    elif guess == snum:
        print("You guessed the secret number!")
        print("It took", count, "number of guesses")
        input("Press enter to exit()")
        exit() #this is generally considered a bad practice way to quit a program


print("Computer has chosen a number between 1 and 10\n\
    Try to guess the number and the computer will tell\n\
    you if your guess was lower or higher than the secret\n\
    number. If you guess the number the computer will tell you\n\
    how many guesses it took.")
doThis()
doThis()
doThis()
doThis()
doThis()
doThis()
doThis()

print("Sorry, you did not guess the number.") 
print("The secret number was", snum)
input("Press enter to exit()")
