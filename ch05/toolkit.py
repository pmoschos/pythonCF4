import functools

ints_list = [26, 5, 4, 3, 2, 1]

def calculate(args):
    def plus():
        return functools.reduce(lambda x, y : x + y, args)
    
    def minus():
        return functools.reduce(lambda x, y: x - y, args)
    
    def mul():
        return functools.reduce(lambda x, y : x * y, args)
    
    def div():
        if not 0 in args[1:]:
            return args[0] / sum(args[1:])
    
    return plus, minus, mul, div

add_func, minus_func, mul_func, div_func = calculate(ints_list)

print("add_func:", add_func())
print("minus_func:", minus_func())
print("mul_func:", mul_func())
print("div_func:", div_func())