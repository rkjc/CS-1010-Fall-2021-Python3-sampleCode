var1 = 0
var2 = 1
print("times table")

while(var2 <=10):
    var1 = 1
    while(var1 <= 10):
        if(var1*var2< 10):
            print( var1*var2, end="  | ")
        else:
            print( var1*var2, end=" | ")
        var1 += 1
    print()
    var2 += 1

print()
print("ALL DONE")
    

