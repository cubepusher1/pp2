from functools import reduce

nums = [1, 2, 3, 4, 5]

# map
squares = list(map(lambda x: x**2, nums))

# filter
evens = list(filter(lambda x: x % 2 == 0, nums))

# reduce
total = reduce(lambda a, b: a + b, nums)

print(squares)
print(evens)
print(total)