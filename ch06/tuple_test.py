# tuple mutability test

my_tuple = (1, 2, [3, "CF"], "Hello")

my_tuple[2] = [1, 2, 3]


print(my_tuple[1])
for item in my_tuple:
    print(id(item), ":", item)

my_tuple[2][0] = 300

print(my_tuple)

for item in my_tuple:
    print(id(item), ":", item)