# don't need to use lambda function with map/filter but often comes in handy
x = [1,2,4,5,3,3,21,2,21,2,313,1,23,143,4]

# map takes all the elements of a list and use a function to map them to a new list

mp = map(lambda i: i + 2, x)    # apply lambda function to each element of x
print(list(mp)) # casting to a list as mp will be of type map, can iterate over that too but usually more useful as a list

# filter will use the lambda function to decide whether an item should be included in the output

fltr = filter(lambda i: i % 2 == 0, x)    # apply lambda function to filter the elements of x
print(list(fltr)) 

# for more complex functions you could define a function, it would be called like this...
def func(i):
    i = i * 3
    return i % 2 == 0

fltr2 = filter(func, x)   
print(list(fltr2)) 