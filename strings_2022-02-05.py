# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# String- ordered, immutable text representation
s1 = 'I\'m an escape character'              # use backslash to escape single quotes
s2 = '''Triple quotes (sgl/dbl)
used for multi-line strings,
or documentation within code.'''
s3 = """A backslash allows a newline within code \
but the output will not"""
print(s3)

# can do slicing of strings using square brackets
print(s1[2:3:2])                            # [start elem : end elem : step size] end elem not included
# use a step of -1 to reverse a string
# concat strings with +
for i in s1:                                # iterate over string's characters
    print(i)
if 'esc' in s1:                             # check if char/substring in string
    print('yes')
s4 = '   Hello World   '                    # spaces will be included in output of string
print(s4.strip())                           # returns string removing extra white space
s4.upper()
s4.lower()
s4.startswith('Hel')                        
s4.endswith('World')
s4.find('orl')                              # returns index of 1st occurence of char/substring
                                            # returns -1 if not found
s4.count('o')                               # count how many occurences of char in string
s4.replace('World','Universe')              # replaces 1st with 2nd, if not found returns orig string
s5 = 'how are you doing'
mylist = s5.split()                         # creates list with 1 word for each element
new_s5 = ' '.join(mylist)                   # join elements of list separating with a space

from timeit import default_timer as timer

my_list = ['a'] * 1000000
# slow way
start = timer()                             # find out how long a section of code takes to run
my_str = ''                                 #
for i in my_list:                           #
    my_str += i                             #
stop = timer()                              # 
print(stop-start)                           # 

# fast way
start = timer()                             
my_str = ''.join(my_list)                   # much faster (30 times?) than above way of concating to a string
stop = timer()                              # 
print(stop-start)                           # 

# Formatiting strings- %, format(), f-Strings

var = "Tom"
my_str = "the variable is %s" % var

var = 3
my_str = "the variable is %d" % var

var = 3.23445645
my_str = "the variable is %f" % var             # by default has 6 decimal places
my_str = "the variable is %.2f" % var           # specify how many decimal places

my_str = "the variable is {}".format(var)
var2 = 6
my_str = "the variable is {:.2f} and {}".format(var, var2)   # 2 decimal places

# f-Strings python v3.6+
my_str = f"the variable is {var} and {var2}"
my_str = f"the variable is { var * 2 } and {var2}"  # curly braces are evaluated at runtime so can perform functions there
print(my_str)