my_list = [1, 2, 3, 4, 5]

a = my_list[0] # indexing
b = my_list[1:] # slicing

print(f"a = {a}, b = {b}")

x, *y = my_list
print(f"x = {x}, y = {y}")

x, *y, z = my_list
print(f"x = {x}, y = {y}, z = {z}")