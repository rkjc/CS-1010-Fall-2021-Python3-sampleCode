
luke = "The quick red fox crushed the chrome window"

print(luke)

count = 0
print('*', end="")
while(count < len(luke)):
    print(luke[count], end="*")
    count += 1
print()


chewy = "sTr1ng5 d4tA with SpAcES"
print( chewy )


bob = chewy.lower()
print( bob )

print( chewy.upper() )
print( chewy )

myentry = input('enter an integer  ')
if( myentry.isnumeric() ):
    myint = int(myentry)
    print(myint + 43)
else:
    print("not an integer")



