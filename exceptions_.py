# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Errors and exceptions
# syntax error (detected by the parser) or an exception

# built-in exceptions
a = 5 + '10'                                            # raises a TypeError
import somerandommodule                                 # ModuleNotFoundError, subclass of import error
b = c                                                   # NameError, var not defined yet
f = open('somefile.txt')                                # FileNotFoundError
a = [1, 2, 3]        
a.remove(4)                                             # ValueError, argument of right type but inappropriate value (4 doesn't exist)                   
a[4]                                                    # IndexError, there is no element 4

# raising an exception
x = -5
if a < 0:
    raise Exception('x should be positive')

# throw an assertion error if assertion is not True
assert(x >= 0), 'x is not poisitve'

# catch exceptions
try:
    a = 5 / 0
except:
    print('an error occured')

try:
    a = 5 / 0
except Exception as e:
    print(e)                                    # prints the system exception error message

# best practice is to specify the type of exception to catch it correctly
try:
    a = 5 / 0
    b = 5 + '10'
except ZeroDivisionError as e:
    print(e)                                    # this exception will be caught, as gets to this first
except TypeError as e:
    print(e)
else:
    print('prints if no exception occured')
finally:                                        # used for cleanup operations- close files/DBs/etc
    print("always prints, whether there's an exception or not")

# create your own exceptions, by creating subclass of Exception class
class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValueTooSmallError('Value too small', x)
try:
    test_value(3)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)

# 2:20:11
