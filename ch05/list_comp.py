grades = [7, 5, 9, 10, 3]

# Map (Transforms the data of the list)
upscaled_grades = [grade + 1 if grade <= 9 else grade for grade in grades]
print("final grades:", upscaled_grades)

# Using map()
upscaled_grades2 = list(map(lambda grade: grade + 1 if grade <= 9 else grade, grades))
print("final grades map():", upscaled_grades2)

# Filter (It is based on a Predicate)
passed_grades = [grade for grade in grades if grade >= 5]
print("Passed:", passed_grades)

# Using filter()
passed_grades2 = list(filter(lambda grade: grade >= 5, grades))
print("Passed filter():", passed_grades2)

print(filter(lambda grade: grade >= 5, grades))