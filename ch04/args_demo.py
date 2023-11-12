# Varargs

def my_add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

def my_avg(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum / len(args)

ages = [27, 35, 42, 18, 20]

print(my_avg(*ages))

print(my_avg(1, 2, 3, 4, 5))
