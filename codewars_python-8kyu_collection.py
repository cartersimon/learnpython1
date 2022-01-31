# https://www.codewars.com/collections/python-8kyu-3
# python-8kyu Collection 

# https://www.codewars.com/kata/56bc28ad5bdaeb48760009b0/python
# remove first and last chars of a string
def remove_char_my(s):
    return s[1:-1]      # s[:-1] get all except last char, s[1:] get all except 1st char

# https://www.codewars.com/kata/51c8991dee245d7ddf00000e/python
# reverse the order of the words in the sentence

def reverse_words_my(s):
    s = s.split(" ")        # split string in the space char
    s.reverse()             # reverse list in place
    s = " ".join(s)         # join words together separated with a space
    return s

def reverseWords_1(str):
    return " ".join(str.split(" ")[::-1])   # str.split(" ")[::-1] ...huh? 

def reverseWords_2(str):
    return ' '.join(reversed(str.split(' ')))   # reversed(str.split(' ')) ...more huh?

def reverseWords(string):
    return ' '.join(reversed(string.split()))   # why did this work? " " is not needed for split()?

# https://www.codewars.com/kata/574b3b1599d8f897470018f6/python
# convert US building floors to UK floor
# US UK
# 1  0
# 0  0
# 5  4
# 12 11
# 14 12
# 15 13
# -3 -3

def get_real_floor_my(n):
    if n <= 0:
        return n
    elif n <= 12:
        return n - 1
    else:
        return n - 2

def get_real_floor_1(n):
    if n <= 0: return n
    if n < 13: return n-1
    if n > 13: return n-2

def get_real_floor_2(n):            # basically same as my solution but laid out differently (it's less clear to me)
    return n if n < 1 else n - 1 if n < 13 else n - 2

def get_real_floor_3(n):
    return n - (n > 0) - (n > 13)   # interesting solution, if n > 0 or n > 13 are True, they evaluate to 1, otherwise 0, and get subtracted!! :)

# https://www.codewars.com/kata/57a0885cbb9944e24c00008e/python
# remove exclaimation marks from a string
def remove_exclamation_marks_my(s):
    return s.replace('!','')

# https://www.codewars.com/kata/57a429e253ba3381850000fb/python
# calculate BMI (weight / height sq) return <=18.5 underweight, <=25 normal, <=30 overweight, >30 obese

def bmi_my(weight, height):
    bmi = weight / (height ** 2)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"

def bmi_1(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

bmi = lambda w,h: (lambda b=w/h**2: ["Underweight", "Normal", "Overweight", "Obese"][(18.5<b) + (25<b) + (30<b)])()

# https://www.codewars.com/kata/582cb0224e56e068d800003c/python
# input is number of hours, consuming 0.5 litres/hour, working out how many litres (rounded down)
def litres_my(time):
    return int(time // 2)

# https://www.codewars.com/kata/58649884a1659ed6cb000072/python
# input current state of traffic light, out what next state will be
# green -> yellow -> red -> green

def update_light_my(current):
    match current:
        case "red": return "green"
        case "yellow": return "red"
        case "green": return "yellow"

# Traceback (most recent call last):
#  File "tests.py", line 2, in <module>
#    from solution import update_light
#  File "/workspace/default/solution.py", line 2
#    match current:
#          ^
# SyntaxError: invalid syntax


print(update_light_my("red"))
print(update_light_my("yellow"))
print(update_light_my("green"))