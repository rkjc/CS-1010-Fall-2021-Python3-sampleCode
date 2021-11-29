
str_input = input("Enter a number to be totaled or 'q' to quit > ")
total = 0
while(str_input != 'q'):
    num_input = int(str_input)
    total += num_input
    str_input = input("Enter a number to be totaled or 'q' to quit > ")

print("The total is", total)
input("Press enter to exit")

