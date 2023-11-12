my_list = [1, 2, "Hello", [3, 4, 5]]

new_list = my_list[:]
print(new_list is my_list)

my_list[0] = 100
print(my_list)
print(new_list)
print("------------")
my_list[3][0] = 300
print(my_list)
print(new_list)