# I am choosing a variable name mpoe which stands for my_parameter_overload_experiment

def mpoe (var1 = None, varDos = None, varC = None):
    if(var1 == None):
        return "no parameters"
    elif(varDos == None):
        return "one param"
    elif(varC == None):
        return "two param"
    else:
        return "three param"


aArr = mpoe (5)
print(aArr)

aArr = mpoe ()
print(aArr)

aArr = mpoe (2, 9)
print(aArr)

aArr = mpoe (9, 23, 3)
print(aArr)



# tempArr = []
# while(inStart < inLimit):
#     tempArr.append(inStart)
#     inStart += 1
# return tempArr