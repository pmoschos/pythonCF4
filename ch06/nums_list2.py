nums = [1, 2, 3, 4, 5, 3, 3, 3]

num_to_find = 20

try:
    index = nums.index(num_to_find)
    print(f"Index of {num_to_find} is: {index}")
except ValueError as e:
    print(e)

num_to_find = 3
count = nums.count(num_to_find)

if count > 0:
    print(f"{num_to_find} is present {count} times in the list")
else:
    print(f"{num_to_find} is not present in the list")