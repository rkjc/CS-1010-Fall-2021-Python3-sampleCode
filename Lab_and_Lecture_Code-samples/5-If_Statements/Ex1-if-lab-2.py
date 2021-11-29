# put your name as a comment at the top of your program

# this statement lets you use the random number generator
import random

# this statement generates an integer from 0 to 20 inclusive
# and stores it in the variable secretNum
secretNum = random.randint(1,20)


print("------------------------------------")

bob = input("enter something")
print("this is what you entered", bob)
print("and here is that random number", secretNum)
