def avg(*args):
    if not len(args):
        return 0
    sum = 0
    for arg in args:
        sum += arg
    return sum / len(args)

my_ints = [10, 5, 9]
print(avg(*my_ints))