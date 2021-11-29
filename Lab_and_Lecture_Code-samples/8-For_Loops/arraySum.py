arr=[[5, 29, 16], [35, 79, 30], [61, 2, 26], [91, 37, 2], [2, 71, 26]]
print (arr)

for x in arr:
    s1 = 0
    for y in x:
        s1 = s1 + y
    print ("sum of ", x, "is", s1)
    print ("average",s1/(len(x)))
