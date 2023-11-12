def avg(*args):
    return sum(args) / len(args) if args else 0

my_ints = [10, 5, 9]
print(avg(*my_ints))