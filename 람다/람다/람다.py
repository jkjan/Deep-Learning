print(list(map(lambda x : x**2, range(5))))

from functools import reduce

print(reduce(lambda x, y : x+y, [0, 1, 2, 3, 4]))


print(list(filter(lambda x : x%2, range(10))))