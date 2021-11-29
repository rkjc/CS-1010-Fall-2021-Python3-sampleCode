import random

for x in range(10):
    print(x, end="-")
    rndy = random.randint(5,100)
    count = 0
    while(count < rndy):
        rnd100 = random.randint(100,999)
        if(rnd100 % 7 == 0):
            print('#', end="")
        else:
            print('*', end="")
        count = count + 1

    print()
