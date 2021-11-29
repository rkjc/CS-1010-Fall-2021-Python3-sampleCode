# richard cross

#Ex4-a
num_list = [34, 42, 99, 1301, 1, 78, 314, 818, 777]


#Ex-B.  Write a program that uses one While Loop to meet the following requirements:


count = 0
while(count < len(num_list)):
    print( num_list[count], end=" " )
    count += 1



#     (a)  print out each of the numbers from the List on the same line.

#     (b)  add up all the numbers in the List and print out the answer on a separate line.
#           (*hint: as you print out each number, add it to a variable to get a running total)

#     (c)  have it print out the largest number in the list.
#            (*hint: try combining the sort and index methods)