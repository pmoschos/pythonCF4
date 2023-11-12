# for scoping

a = range(10)
print(a)
print(type(a))

for i in a:
    print(i, end=" ")
print("\n----")
print(i)

for index, value in enumerate(range(10)):
    print(index, ":", value)