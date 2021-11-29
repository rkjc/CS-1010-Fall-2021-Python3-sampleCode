
# basic use of a range statement in a for loop
# range( A )
# create List of integers that starts at zero and counts up to but not including integer A
for count in range(5):
    print(count)

print('---------------------')

# range statement stored in a variable passed to the loop
myRng1 = range(5)
for c in myRng1:
    print(c)

print('---------------------')

# two attribute range statement in a for loop
# range( A , B )
# integer A is the first element in the generated list
# integer B is the limit up to, but not included, in the list
for count in range(2, 5):
    print(count)

print('---------------------')

# three attribute range statement in a for loop
# range( A , B , C )
# integer A is the first element in the generated list
# integer B is the limit up to, but not included, in the list
# integer C is the ammount to increment each step
for count in range(1, 9, 2):
    print(count)

print('---------------------')

# three attribute range statement can also decriment
for count in range(12, 3, -2):
    print(count)

print('---------------------')
# NOTE
# range(int) does not generate a list
# it is a function that acts like a list of integers when used as a list
# when printed it just prints the function signature
print( range(7) )