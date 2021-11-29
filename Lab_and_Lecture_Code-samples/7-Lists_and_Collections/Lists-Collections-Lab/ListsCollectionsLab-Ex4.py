num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]
total = 0
count = 0
while count < len(num_list):
    temp_num = num_list[count]
    total += temp_num
    print(temp_num, end=" ")
    count += 1
print()

print("Total =", total)
num_list.sort()
largest_num = num_list.pop()
print("Largest element =", largest_num)
print("-------------------------")
num_list = [3, 7, 999, 1981, 1066, -4086, 33]
total = 0
count = 0
while count < len(num_list):
    temp_num = num_list[count]
    total += temp_num
    print(temp_num, end=" ")
    count += 1
print()

print("Total =", total)
num_list.sort()
largest_num = num_list.pop()
print("Largest element =", largest_num)