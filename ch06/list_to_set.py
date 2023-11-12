my_list = [1, 2, 3, 4, 5, 1, 1, 2, 1, 4]

unique_list = list(set(my_list)) # Pythonian way
print(unique_list)

print("-------------------")

# give me the list of diff elements (each element once)
unique_list = []
for item in my_list:
    if not item in unique_list:
        unique_list.append(item)

print(unique_list)