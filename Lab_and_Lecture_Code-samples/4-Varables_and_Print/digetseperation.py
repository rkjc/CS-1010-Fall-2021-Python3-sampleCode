happyInputStr = input("enter a number ")
x = int( happyInputStr )

dig_1 = x % 10

x = int(x/10)
dig_2 = x % 10

x = int(x/10)
dig_3 = x % 10

x = int(x/10)
dig_4 = x % 10

x = int(x/10)
dig_5 = x % 10

print("the disected number digits are ", dig_5, dig_4,  dig_3,  dig_2,  dig_1)

