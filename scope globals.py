x = 'tim'

def func(name):
    x = name    # this will NOT affect the value of x

def func2(name):
    global x    # by using the 'global' cmd, it WILL affect the value of x
    x = name    # recommended not to use 'global' unless absolutely necessary

print(x)
func('changed')
print(x)
func2('changed')
print(x)