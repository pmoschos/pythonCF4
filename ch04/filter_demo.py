# filter and lambda

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers_iterator = filter(lambda x: x % 2 == 0, numbers)

for num in even_numbers_iterator:
    print(num, end=" ")

# convert the iterator to list
even_numbers_list = list(filter(lambda x: x % 2 == 0, numbers))
print()
print(even_numbers_list)
print(even_numbers_list)
print(even_numbers_list)