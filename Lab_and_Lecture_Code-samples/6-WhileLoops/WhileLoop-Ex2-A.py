my_total = 0
print(my_total)
count = 1
while count <= 100:
    old_total = my_total
    my_total += count
    print(old_total, "+", count, "=", my_total)
    count += 1
