# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Tools for handling iterators (iterators can be used in a for loop- lists, etc) 
# itertools- product, permutations, combinations, accumulate, groupby, infinite iterators

from itertools import product
a = [1, 2]
b = [3, 4]
prod1 = product(a,b)                                # calculates the Cartesian product 
print(prod1)                                        # outputs a product object
print(list(prod1))                                  # to see the contents, convert to a list
# [(1, 3), (1, 4), (2, 3), (2, 4)]
c = [1, 2]
d = [3]
prod2 = product(c,d, repeat = 2)                    # repeats the Cartesian product 
print(list(prod2))
# [(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]

from itertools import permutations

# 1:39:29


from itertools import combinations
from itertools import accumulate
from itertools import groupby
