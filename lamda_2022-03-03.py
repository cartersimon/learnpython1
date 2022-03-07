# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Lambda functions... typically used when have a simple function that's needed just once
# or as an argument to a higher order function (higher order function- a function that takes another function as an arguments), such as sorted/map/filter/reduce/etc
# lambda arguments: expression

def add10_func(x):                                                              # this function declaration is the same as the lambda function below
    return x + 10

add10 = lambda x: x + 10                                                        # variable holds the function to be able to call it later
print(add10(5))

mutl = lambda x,y: x*y

points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]

# sorted
points2D_sorted = sorted(points2D)
print(points2D_sorted)
# by default this sorts by value of 1st value in pair but can give a rule on how to sort
points2D_sorted2 = sorted(points2D, key= lambda x: x[1])                        # sort by the 2nd value
points2D_sorted3 = sorted(points2D, key= lambda x: x[0] + x[1])                 # sort by the sum of the tuple

# map(func, seq) 
a = [1, 2, 3, 4, 5, 6]
b = map(lambda x: x*2, a)                                                       # map the lambda function onto the list "a"
print(list(b))
c = [x*2 for x in a]                                                            # for this particular example, prob easier to use list comprehension
print(c)

# filter(func, seq)                                                             # func evaluates all items in seq to True/False, returning the True items
b2 = filter(lambda x: x%2 == 0, a)                                              # map the lambda function onto the list "a"
print(list(b2))

c2 = [x for x in a if x % 2 == 0 ]                                              # again this can be done via list comprehension

# reduce(func, seq)                                                             # repeatedly applies func to seq to return a single value

from functools import reduce
product_a = reduce(lambda x,y: x*y, a)                                          # reduce function always has 2 arguments

print(product_a)