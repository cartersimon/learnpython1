# f strings new in v3.6
# used to manipulate and create strings

tim = 89
x = f'hello {6 + 8} {tim}'  # items within curly braces will be evaluated, no need to concat and convert to string with 'str()'
print(f'Hello {tim}')