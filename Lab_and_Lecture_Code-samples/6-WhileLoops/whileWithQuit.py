invar = 0
total = 0

invar = input("Please enter a number or 'q' to quit > ")

while(invar != 'q'):
    invar = int(invar)
    total = total + invar
    print("Your subtotal is", total)
    invar = input("Please enter a number or 'q' tp quit >  ")


print("Your total is", total)
