# crud functions in list
grades = [1, 4, 8, 3, 9, 5]

# Append
grades.append(10) # [1, 4, 8, 3, 9, 5, 10]

# Update
grades[1] = 5 # [1, 5, 8, 3, 9, 5, 10]

# delete
if 5 in grades:
    grades.remove(5) # [1, 5, 8, 3, 9, 5, 10]

if 2 in grades:
    print("Index of 10:", grades.index(2)) # [1, 8, 3, 9, 5, 10]

#for grade in grades:
#    print(grade)

