import random
snum = random.randint(1,10)
count = 0
notDone = True

print("Computer has chosen a number between 1 and 10\n\
    Try to guess the number and the computer will tell\n\
    you if your guess was lower or higher than the secret\n\
    number. If you guess the number the computer will tell you\n\
    how many guesses it took.")

# this first check always happens
guess = int(input("Try to guess the secret number > "))
count += 1
if guess < snum:
    print("Your guess was less than the secret number.")
elif guess > snum:
    print("Your guess was greater than the secret number.")
elif guess == snum:
    print("You guessed the secret number!")
    print("It took", count, "number of guesses")
    # setting this to False skips all the following guesses
    notDone = False

# these check programs only happen if the notDone variable is still True
if notDone == True:    
    guess = int(input("Try to guess the secret number > "))
    count += 1
    if guess < snum:
        print("Your guess was less than the secret number.")
    elif guess > snum:
        print("Your guess was greater than the secret number.")
    elif guess == snum:
        print("You guessed the secret number!")
        print("It took", count, "number of guesses")
        # setting this to False skips all the following guesses
        notDone = False

# these check programs only happen if the notDone variable is still True
if notDone == True:    
    guess = int(input("Try to guess the secret number > "))
    count += 1
    if guess < snum:
        print("Your guess was less than the secret number.")
    elif guess > snum:
        print("Your guess was greater than the secret number.")
    elif guess == snum:
        print("You guessed the secret number!")
        print("It took", count, "number of guesses")
        # setting this to False skips all the following guesses
        notDone = False

# these check programs only happen if the notDone variable is still True
if notDone == True:    
    guess = int(input("Try to guess the secret number > "))
    count += 1
    if guess < snum:
        print("Your guess was less than the secret number.")
    elif guess > snum:
        print("Your guess was greater than the secret number.")
    elif guess == snum:
        print("You guessed the secret number!")
        print("It took", count, "number of guesses")
        # setting this to False skips all the following guesses
        notDone = False

# these check programs only happen if the notDone variable is still True
if notDone == True:    
    guess = int(input("Try to guess the secret number > "))
    count += 1
    if guess < snum:
        print("Your guess was less than the secret number.")
    elif guess > snum:
        print("Your guess was greater than the secret number.")
    elif guess == snum:
        print("You guessed the secret number!")
        print("It took", count, "number of guesses")
        # setting this to False skips all the following guesses
        notDone = False

if notDone == True:
    print("Sorry, you did not guess the number.") 
    print("The secret number was", snum)
else:
    print("Thank you for playing")

input("Press enter to exit()")
