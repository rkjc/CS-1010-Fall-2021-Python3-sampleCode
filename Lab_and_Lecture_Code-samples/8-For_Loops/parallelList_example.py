# make a couple of lists
fruits = ['banana', 'apple',  'mango', 'orange', 'grape', 'pumpkin', 'lemon']
fruitColors = ['yellow', 'red', 'dark-yellow', 'orange', 'purple', 'orange', 'light-yellow']

# get the number of elements in the list
numOfFruit = len(fruits)

# make a range function using the number of elements
myRan = range(numOfFruit)

# loop through the generated range function and use it as an index
for c in myRan:
    print(c, fruits[c], fruitColors[c])



