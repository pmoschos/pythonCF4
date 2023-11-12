my_list = [1, 2, "Hello", [3, 4, 5]]

new_list = my_list * 2 # [1, 2, "Hello", [3, 4, 5], 1, 2, "Hello", [3, 4, 5]]
print(new_list)
print("---------------")
new_list[0] = 100
print(new_list)
print("---------------")
new_list[3][0] = 300
print(new_list)

for item in new_list:
    print(item, ":", id(item))
