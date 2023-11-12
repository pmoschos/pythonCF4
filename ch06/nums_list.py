nums = [1, 2, 3, 4, 5]

num_to_find = 2

if num_to_find in nums:
    print("Found")
    index = nums.index(num_to_find)
    print(f"Index of {num_to_find} is: {index}")
else:
    print("Not found")

