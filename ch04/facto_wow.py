from functools import reduce

n = int(input("Give an int to calc facto: "))

result = reduce(lambda x, y : x * y, range(1, n + 1))

print(f"{n}! = {result}")