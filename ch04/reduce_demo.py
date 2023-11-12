from functools import reduce

# list of numbers
my_ints = [1, 2, 3, 4, 5]

result = reduce(lambda x, y : x * y, my_ints)

print("Result:", result)