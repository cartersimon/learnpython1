# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Collections- Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import OrderedDict         # As a normal Dict but remembers order items were added
od1 = OrderedDict()
od1['b'] = 2
od1['c'] = 3
od1['d'] = 4
od1['a'] = 1
od2 = {}                                    # Though since v3.7 Dict also remembers order
od2['b'] = 2
od2['c'] = 3
od2['d'] = 4
od2['a'] = 1
# od1 & od2 both keep order added...   {'b' : 2, 'c' : 3, 'd' : 4, 'a' : 1}

from collections import defaultdict         # As a normal Dict but has a default value if key not set
                                            # avoids raising a key error
dd1 = defaultdict(int)                      # returns default int value (0) if try to access non-existant key
# default values... float: 0.0, list: [], etc

from collections import deque               # A double-ended queue, can add/remove elements from both ends
deq1 = deque()
deq1.append(1)                              # add item to end of queue (as usual)... deque([1])
deq1.append(2)                              # add item to end of queue... deque([1, 2])
deq1.appendleft(3)                          # add item to beginning of queue... deque([3, 1, 2])
deq1.pop()                                  # removes last item... deque([3, 1])
deq1.popleft()                              # remove first item... deque([1])
deq1.extend([4, 5, 6])                      # add list to the end... deque([1, 4, 5, 6])
deq1.extendleft([7, 8, 9])                  # add list to the beginning... deque([9, 8, 7, 1, 4, 5, 6])
# notice that above adds the 7 to the left, then the 8, then the 9
# so the beginning will have [9, 8, 7], rather than [7, 8, 9]
deq2 = deque()                              
deq2.append(1)
deq2.append(2)
deq2.appendleft(3)                          # contains deque([3, 1, 2])
deq2.rotate(1)                              # move all elements 1 place to the right
# deque ([2, 3, 1]) ...enter a negative number to rotate to the left



