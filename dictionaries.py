# https://www.youtube.com/watch?v=HGOBQPFzWKo&list=RDCMUC8butISFwT-Wl7EV0hUK0BQ&start_radio=1&t=181s
# Intermediate Python Programming Course (freecodecamp.org)

# Key-Value pairs, unordered, mutable (can add/change elements)
# Keys can be string, integer, or tuple(if tuple contains immutable elements)

# create dict...
mydict = {"name": "Max", "age": "28", "city" : "New York"}
mydict2 = dict(name= "Mary", age= "27", city= "Boston")         # can also created with dict(), no quotes needed for key, uses equals instead of colon
value = mydict["age"]                                           # get value by stating the desired key 

# add K-V to dict...
mydict["email"] = "max@xyz.com"                                 # add a new K-V pair to the dict
mydict["email"] = "newmax@xyz.com"                              # K-V already exists so will overwrite the value held by that Key

# remove K-V from dict...
del mydict["email"]                                             # delete a K-V (note square brackets)
mydict.pop("email")                                             # deletes & returns a K-V (note normal brackets)
mydict.popitem()                                                # deletes the last K-V (LIFO) and returns it

# check if Key is in dict...
if "name" in mydict:
    print(mydict["name"])

try:
    print(mydict["name"])
except:
    print("Error")

# looping thru dict...
for key in mydict:                                              # iterate thru all keys
    print(key)

for key in mydict.keys():                                       # iterates all keys (mydict.keys() return a list with all keys inside)
    print(key)

for value in mydict.values():                                   # iterate thru all values
    print(value)

for key, value in mydict.items():                               # iterate over keys and values
    print(key, value)

# copying dict...
mydict_cpy = mydict                                             # copies ref to the dict, so both pointing to same dict
mydict_cpy = mydict.copy()                                      # an actual copy of the dict
mydict_cpy = dict(mydict)                                       # another way

# merge 2 dicts...
mydict = {"name": "Max", "age": "28", "email" : "tim@xyz.com"}
mydict2 = dict(name= "Mary", age= "27", city= "Boston")
mydict.update(mydict2)                          # overwrites existing keys of mydict and adds any that weren't present and any keys in mydict but not in mydict2 remain untouched
# Output... {'name': 'Mary', 'age': '27', 'email': 'tim@xyz.com' , 'city': 'Boston'}

mytuple = [8, 7]                                                # this is not valid, this is a list (which is mutable) throws not hashable error, so can't be used as a Key
mytuple = (8, 7)                                                # this is fine, this is a tuple (immutable), so can be used as a Key
mydict = {mytuple: 15}
