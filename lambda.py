# lambda- a one-line, anonymous function
x1 = lambda x: x + 5  # (not the recommended way to use lambdas, commonly used for map & filter)
x2 = lambda x, y: x + y  # (not the recommended way to use lambdas, commonly used for map & filter)

print(x1(2))
print(x2(2, 32))