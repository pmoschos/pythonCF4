def add(a = 1, b = 2, c = 3):
    return a + b + c

print(add(10)) # 15
print(add(10, 20)) # 33
print(add(10, 20, 30)) # 60
print(add(a = 10)) # 15
print(add(b = 20)) # 24
print(add(c = 30)) # 33
print(add(c = 30, a = 10)) #42
