# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Tools for handling iterators (iterators can be used in a for loop- lists, etc) 
# itertools- product, permutations, combinations, accumulate, groupby, infinite iterators

from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)                          # create all permutations of the elements
perm = permutations(a, 2)                       # permutations with combinations of 2 elements
print(list(perm))

from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)                       # returns unique combinations, length arg required
print(list(comb))
comb_wr = combinations_with_replacement(a, 2)   # as combinations but can duplicate elements 

from itertools import accumulate
# creates an iterator that returns acculumated sums, or other binary functions
a = [1, 2, 3, 4]
acc = accumulate(a)                             
# Output... [1, 3, 6, 10]

# by default adds values but can apply function
import operator
acc2 = accumulate(a, func=operator.mul())       # multiplies values
a = [1, 2, 5, 3, 4]
acc2 = accumulate(a, func=max())                # get maximum value
# output... [1, 2, 5, 5, 5]

from itertools import groupby
# creates an iterator that returns keys and groups from an iteratable
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
grp_obj = groupby(a, key=smaller_than_3)
# creates 2 groups (lists), values that match the key, and those that don't
for key, value in grp_obj:
    print(key,list(value))
# Output...
# True [1, 2]
# False [3, 4]

# could also use a llambda function for the key...
grp_obj2 = groupby(a, key=lambda x: x < 3)
for key, value in grp_obj2:
    print(key,list(value))

people = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
        {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
grp_obj3 = groupby(people, key=lambda x: x['age'])
for key, value in grp_obj3:
    print(key,list(value))
# Output...
# 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
# 27 [{'name': 'Lisa', 'age': 27}]
# 28 [{'name': 'Claire', 'age': 28}]

# some infinite iterators...
from itertools import count, cycle, repeat
for i in count(10):                                                     # creates a count from 10 to infinity
    print(i)
    if i == 15:                                                         # break at 15
        break

b = [1, 2, 3]
for i in b:
    print(i)                                                            # cycles thru all values in the list infinitely
# Output... 
# 1
# 2
# 3
# 1
# 2
# etc...

for i in repeat(1):                                                     # outputs 1 infinitely
    print(i)

for i in repeat(1, 4):                                                  # outputs 1 four times
    print(i)