# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Sets- unordered, mutable, no duplicates

# create a set...
myset = {1, 2, 3, 1}    # if you put a duplicate value it allows but ignores it
myset = set([1, 2, 3])  # alternative way to create a set
myset = set("Hello")    # places the characters of the string into a set
# Output... {'o', 'l', 'H', 'e'}
myset = {}              # this creates an empty _dict_!
myset = set()           # use the set() funtion to create an empty set

# add elements...
myset.add(3)
myset.add(2)
myset.remove(3)
myset.remove(9)         # value not in set throws a KeyError
myset.discard(9)        # value not in set, no error thrown
myset.clear()           # empty the set
myset.pop(3)            # remove value from set and return it
# iterate sets using for loop

# check for values...
if 2 in myset:
    print("yes")

# below functions make no changes to the sets, just return a new set
# union (combine elements from 2 sets)...
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
# Output... {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

# intersection (finds elements found in both sets only)...
p = odds.intersection(primes)
# Output... {3, 5, 7}

# difference (returns elements in 1st set that aren't in 2nd)...
diff = evens.difference(primes)
# Output... {0, 8, 4, 6}

# symetric difference (takes elements in 1st and 2nd sets, excludes any in both)...
sdiff = evens.symmetric_difference(primes)
print(sdiff)
# Output... {0, 3, 4, 5, 6, 7, 8}

# below functions will modify the set in-place
odds.update(evens)                  # adds the elements of one set to another
odds.intersection_update(primes)    # keep only the elements found in both sets
odds.difference_update(primes)      # remove elements found in other set
odds.symmetric_difference_update(primes)    # elements from both sets, excluding elements common to both

setA = {1, 2, 3}
setB = {1, 2, 3, 4, 5, 6}
setA.issubset(setB)                 # A is a subset of B returns true if all elements of A are in B
setA.issuperset(setB)               # A is superset of B true if A contains all the elements of B
setA.isdisjoint(setB)               # true if contains no common elements

# copying...

setA = setB                         # as with lists, copies ref to set, rather than creating a copy
setA = setB.copy()                  # creates a copy of setB to assign to setA
setA = set(setB)                    # alternative way to copy a set

# frozen set- an immutable set
a = frozenset([1, 2, 3, 4])