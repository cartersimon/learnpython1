def function_name(x, y):    # declare the function
    print('Inside funct', x, y)
    # can define functs within a functs
    #return x * y
    return x * y, x / y # this returns a tuple

def f2(x, y, z=None):   # z is optional
    print("in funct f2")
    print(x, y, z)
    if z != None:
        print(x, y, z)
    else:
        print(x, y)
    # it seems that the value gets remembered??

print(function_name(5, 6)) # call the function
r1, r2 = function_name(5, 6) 
    # returned values go into separate variables
print(r1, r2)
f2(3, 6)
f2(4, 7, 2)