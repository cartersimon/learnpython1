# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# ordered collection that is immutable (can't be changed), allows duplicate elements
# when working with large data tuple can be more efficient than lists
# can be more efficient to create and iterate over a tuple than a list

mytuple = ("Max", 28, "Boston")     # create tuple
mytuple = "Max", 28, "Boston"       # brackets are optional
mytuple = ("Max")                   # if want one element tuple, this doesn't work, recognised as a string
mytuple = ("Max",)                  # for one element tuple need to add a comma
mytuple = tuple(["Max", 28, "Boston"])  # create tuple from a list

item = mytuple[0]                   # get first element of tuple
mytuple[0] = "Bob"                  # throws error, obj does not support item assignment

for i in mytuple:                   # iterate over tuple
    print(i)
if "Max" in mytuple:                # check if value in tuple
    print("yes")

mynewtuple = ('a', 'p', 'p')
mynewtuple.count('p')               # count number of times value found in tuple
mynewtuple.index('p')               # get index of first occurence of value in tuple
mynewtuple.index('o')               # throws an error(?!) trying to find non-existant value in tuple

my_list = list(mytuple)             # create list from tuple
tuple2 = tuple(my_list)             # create tuple from list

# slicing is same as lists

# unpacking
name, age, city = mytuple           # assign name to first element, age to 2nd element, 3rd to city
name, age = mytuple                 # throws an error, too many values to unpack
tuple3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
i1, *i2, i3 = tuple3                # i1 assigned first element, i3 assigned last element, i2 assigned array of all other remaining elements

import sys                              # even though tuple and list contain the same data, the tuple is smaller
my_list = [0, 1, 2, "hello", True]
my_tuple = [0, 1, 2, "hello", True]
print(sys.getsizeof(my_list), "bytes")  # output... 104 bytes
print(sys.getsizeof(my_tuple), "bytes") # output... 88 bytes

import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))     # time how long to create a list 1000000 times (list takes longer)
print(timeit.timeit(stmt="([)0, 1, 2, 3, 4, 5)", number=1000000))   # time how long to create a tuple 1000000 times 