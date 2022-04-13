from functools import reduce


s = [1, 2, 3, 4]
x = reduce(lambda x, y: x+y, s)
print(x)