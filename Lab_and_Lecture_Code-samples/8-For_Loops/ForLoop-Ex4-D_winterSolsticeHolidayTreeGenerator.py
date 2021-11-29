 
import random
print("-----------\n\n")

line_count = int(input("enter height > "))
# line_count = int("8")

for temp_count in range(1, line_count + 1):
    chr_count = (temp_count * 2) - 1
    space_count = line_count - temp_count
    print(' ' * space_count, end="")
    for chr_pos in range(chr_count):
        rand_num = random.randint(1,temp_count)
        if temp_count == 1:
            print("\u2738", end="")
        elif rand_num == 1:
            print("0", end="")
        else:
            print( '^', end="")
    print()

for trunk_row in range(3):
    trunk_space = int(line_count - 3)
    print(' ' * trunk_space, '###')


print("-" * (line_count * 2))


input("press enter to quit")
