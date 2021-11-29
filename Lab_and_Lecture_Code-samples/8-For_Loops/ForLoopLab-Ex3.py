print("Run #1")
my_list = [4, 76, 2, 234, 9, 71]
largest_num = 0
total = 0
print("Input list is: ", end="")
for temp_num in my_list:
    print(temp_num, end=", ")
    total += temp_num
    if temp_num > largest_num:
        largest_num = temp_num
print()
print("Sum =", total)
print("Average = ", total/(len(my_list)))
print("Largest number is", largest_num)
print("--------------------------")
print("Run #2")
my_list = [3, -17, 99, -32, 321, 62, 27]
largest_num = 0
total = 0
print("Input list is: ", end="")
for temp_num in my_list:
    print(temp_num, end=", ")
    total += temp_num
    if temp_num > largest_num:
        largest_num = temp_num
print()
print("Sum =", total)
print("Average = ", total/(len(my_list)))
print("Largest number is", largest_num)
print("--------------------------")
print("Run #3")
my_list = [1899, 1978, 23, 0, 23, 37, 237, 8, 2, -77, 31]
largest_num = 0
total = 0
print("Input list is: ", end="")
for temp_num in my_list:
    print(temp_num, end=", ")
    total += temp_num
    if temp_num > largest_num:
        largest_num = temp_num
print()
print("Sum =", total)
print("Average = ", total/(len(my_list)))
print("Largest number is", largest_num)
print("--------------------------")