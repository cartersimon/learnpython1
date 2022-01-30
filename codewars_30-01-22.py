## Below are katas from the following collection... https://www.codewars.com/collections/python-8kyu

# https://www.codewars.com/kata/5aa736a455f906981800360d/python
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1] 

# https://www.codewars.com/kata/555086d53eac039a2a000083/python
# if f1 is odd and f2 is even, or vice versa, then return True
def lovefunc_my( flower1, flower2 ):
    return (flower1 % 2 == 0 and flower2 % 2 != 0) or (flower1 % 2 != 0 and flower2 % 2 == 0)

def lovefunc_1( flower1, flower2 ):
    return (flower1+flower2) % 2

def lovefunc_2(flower1, flower2):
    return flower1 % 2 != flower2 % 2

# https://www.codewars.com/kata/55a70521798b14d4750000a4/python
def greet_my(name):
    return f"Hello, {name} how are you doing today?"

def greet_1(name):
    return "Hello, {} how are you doing today?".format(name)

def greet_2(name):
    return "Hello, %s how are you doing today?" % name

# https://www.codewars.com/kata/568d0dd208ee69389d000016/python
# Each day costs $40. 7 or more, $50 off total. 3 or more days, $20 off total
# Write a code that gives out the total amount for different days(d)
def rental_car_cost_my(d):
    total = d * 40
    if d >= 7:
        return total - 50
    elif d >= 3:
        return total -20
    else:
        return total

def rental_car_cost_1(d):
    total = d * 40
    if d >= 7:
        total -= 50
    elif d >= 3:
        total -= 20
    else:
        return total

def rental_car_cost_2(d):
    discount = 0
    if d >= 7:
        discount = 50
    elif d >= 3:
        discount = 20
    return d * 40 - discount

# https://www.codewars.com/kata/56f699cd9400f5b7d8000b55/python
# switch the first and last elements of an array
def fix_the_meerkat_my(arr):
    head = [arr[0]]
    tail = [arr[-1]]
    arr.pop(0)
    arr.pop(-1)
    return tail + arr + head

def fix_the_meerkat_1(arr):
    return arr[::-1]    # *** find out WTF is happening here!!

def fix_the_meerkat_2(arr):
    arr.reverse()
    return arr

# https://www.codewars.com/kata/5715eaedb436cf5606000381/python
# sum all the +ve numbers of an array, if no +ve numbers return 0
def positive_sum_my(arr):
    sum = 0
    for a in arr:
        if a >= 0:
            sum += a
    return sum

def positive_sum_1(arr):
    return sum(x for x in arr if x > 0) # *** investigate the workings of this structure
    # return x if x > 0 for all values in arr

def positive_sum_2(arr):
    return sum(filter(lambda x: x > 0,arr)) # *** spend more time working with lambda functions

# https://www.codewars.com/kata/577bd026df78c19bca0002c0/python
# change '5' to 'S', '0' to 'O' & '1' to 'I'
def correct_my(s):
    chlist = list(s)  # using list() to create an array from the string
    output = []

    for c in chlist:
        if c == '5':
            output.append('S')
        elif c == '0':
            output.append('O')
        elif c == '1':
            output.append('I')
        else:
            output.append(c)
    return ''.join([str(item) for item in output])    # a list comprehension to convert back to a string

def correct_1(string):
    return string.translate(str.maketrans("501", "SOI"))    # investigate 'maketrans' and 'translate' functions

def correct_2(string):
    return string.replace('1','I').replace('0','O').replace('5','S')    # it seems there's a built-in replace function for strings- investigate

# https://www.codewars.com/kata/57cc975ed542d3148f00015b/python
# if value is in array return True (value can be a string or number)
def check_my(seq, elem):
    return elem in seq


# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/python
# sort vector of strings alphabetically (based on ASCII value) and return first value as a string with '***' between each letter. Don't add/remove array elements
def two_sort_my(array):
    array.sort()
    return '***'.join(array[0])

def two_sort_1(array):
    return '***'.join(min(array))

# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/python
# split string into an array of words
def string_to_array_my(s):
    return s.split(" ")

# https://www.codewars.com/kata/57f780909f7e8e3183000078/python
# multiply integer array values
def grow_my(arr):
    total = 1
    for i in arr:
        total *= i
    return total

from functools import reduce
def grow_1(arr):
    return reduce(lambda x, y: x * y, arr)  # practice lambda functions and look up reduce function

# https://www.codewars.com/kata/588417e576933b0ec9000045/python
# calc how many ppl you will block on the way out of the cinema. Inputs are #rows, #columns, and your row & column. 
# Total all the rows behind your row all the way to the end column
# if your seat is col 5, row 3 (and cinema has 16 columns & 11 rows) then you will disturb everyone in... 
# columns 5 -> 16 and rows 3 -> 11 (add one to column to account for your row)
# i.e. (16 - 5) * (12 - 3) people = 12 * 9 = 96
def seats_in_theater_my(tot_cols, tot_rows, col, row):
    return ((tot_cols - col + 1) * (tot_rows - row))

# https://www.codewars.com/kata/59342039eb450e39970000a6/python
# given a number, return the number of positive odd numbers less than that number
# oddCount(7) there are 3 odd numbers less than 7, i.e [1, 3, 5]. 7/2 = 3.5
# oddCount(8) there are 4 odd numbers less than 8, i.e [1, 3, 5, 7]. 8/2 = 4
def oddCount_my(n):
    return int(n/2)

def oddCount_1(n):
    return n // 2

# https://www.codewars.com/kata/5b077ebdaf15be5c7f000077/python
# input is a positive integer, 3 for example, output is "1 sheep...2 sheep...3 sheep..."
def count(n):
    
    return 