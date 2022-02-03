# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

mylist = [4, 0, 3, 10, -4]

mylist.sort()               # sort in-place
mynewlist = sorted(mylist)  # mylist remain unsorted, mynewlist will be sorted
mylist = [0] * 5
new_list = mylist + mynewlist

# slicing
mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:4]             # grab elements 1 to 3 (4th element not included)
# output... [1, 2, 3]
a = mylist[:4]              # grab elements from beginning to 3
# output... [0, 1, 2, 3]
a = mylist[1:]              # grab elements from 1 to end
# output... [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[::2]             # define step, grab every 2nd element
# output... [0, 2, 4, 6, 8]
a = mylist[::-1]            # reverse list
# output... [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

mynewlist = mylist          # this does create a 'copy' of the array BUT it copies the reference to the array, so actually the same list
mynewlist = mylist.copy()   # copy all elements into mynewlist
mynewlist = mylist[:]       # mynewlist takes slice from beginning to end, i.e. copies all elements
mynewlist = list(mylist)    # create new array mynewlist with all elements of mylist, i.e. copy all elements

# list comprehension (create list from existing list on 1 line)
mynewlist = [ i*i for i in mylist ]  # copy each element of mylist, squaring it during the copy