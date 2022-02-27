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
grp_obj = groupby(a, key=)

# 1:46:18