print()
print("Think of a number between 0 and 100 inclusive\n")
print("The program will print out a number and wait for your input\n")
print("If the number is lower than your secret number enter the character L")
print("If the number is higher than your secret number enter the character H")
print("If the number is equal to your secret number enter the character E")
print("The program gets 7 chances to guess your number")
print("If it guesses your number it will print out the number of guesses it took")
print()



highRemain = 10
lowRemain = 1
span = highRemain - lowRemain
guess = round(span / 2)
count = 0

print("Is this your number? ", guess)
count += 1
responce = input("Is your number High, Low, or Equals to the Guess >> ")
# the H response means the secret number is Higher than the guessed number
if(responce == 'H'):
    lowRemain = guess + 1
    span = highRemain - lowRemain
    guess = round(span / 2) + lowRemain
# the L response means the secret number is Lower than the guessed number
if(responce == "L"):
    highRemain = guess - 1
    span = highRemain - lowRemain
    guess = round(span / 2) + lowRemain
if(responce == "E"):
    print("It took", count, "tries to guess your number")
    print("thanks for playing")
else:
    print("Is this your number? ", guess)
    count += 1
    responce = input("High, Low, Equals >> ")
    if(responce == 'H'):
        lowRemain = guess + 1
        span = highRemain - lowRemain
        guess = round(span / 2) + lowRemain
    if(responce == "L"):
        highRemain = guess - 1
        span = highRemain - lowRemain
        guess = round(span / 2) + lowRemain
    if(responce == "E"):
        print("It took", count, "tries to guess your number")
        print("thanks for playing")
    else:
        print("Is this your number? ", guess)
        count += 1
        responce = input("High, Low, Equals >> ")
        if(responce == 'H'):
            lowRemain = guess + 1
            span = highRemain - lowRemain
            guess = round(span / 2) + lowRemain
        if(responce == "L"):
            highRemain = guess - 1
            span = highRemain - lowRemain
            guess = round(span / 2) + lowRemain
        if(responce == "E"):
            print("It took", count, "tries to guess your number")
            print("thanks for playing")
        else:
            print("Is this your number? ", guess)
            count += 1
            responce = input("High, Low, Equals >> ")
            if(responce == 'H'):
                lowRemain = guess + 1
                span = highRemain - lowRemain
                guess = round(span / 2) + lowRemain
            if(responce == "L"):
                highRemain = guess - 1
                span = highRemain - lowRemain
                guess = round(span / 2) + lowRemain
            if(responce == "E"):
                print("It took", count, "tries to guess your number")
                print("thanks for playing")
            else:
                print("was not able to guess it")