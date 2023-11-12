def my_add(a, b):
    if not ((isinstance(a, int) or isinstance(a, float)) and 
            (isinstance(b, int) or isinstance(b, float))):
        return 0
    return a + b

def my_add2(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return 0
    return a + b

print(my_add(10, 20))
print(my_add(5, 8.3))
print(my_add("Hello ", 0))
print(my_add("Hello ", "Coding Factory"))