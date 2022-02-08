# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Collections- Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import Counter
a = "aaaaabbbbccc"
my_counter = Counter (a)
print(my_counter)                           # creates a dict with a count of each value, so {'a': 5, 'b' : 4, 'c' : 3} (within a Count type variable)
print(my_counter.items())                   # get just the K-V pairs
print(my_counter.most_common(1))            # gets the (1st) most common key, returns a list with tuples inside... [('a', 5)]
print(my_counter.most_common(1)[0])         # returns... ('a', 5)
print(my_counter.most_common(1)[0][0])      # returns.... a
print(list(my_counter.elements()))          # .elements returns pointer to a list, so use list() function to view the elements


from collections import namedtuple          # easy, lightweight colelction type (similar to a struct??)
Point = namedtuple('Point', 'x,y')          # creates a calss called 'Point', with fields 'x' and 'y'
pt = Point(1, -4)
print(pt)                                   # Output... Point(x=1, y=-4)

# 1:28:46