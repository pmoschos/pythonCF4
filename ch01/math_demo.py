import math

name = "Alice"
age = 20

print("CF")
print("PI =", math.pi)
print(name + " is " + str(age) + " years old")

# Python 2 style
print("PI = %10.5f" % math.pi)
print("%s is %d years old" %(name, age))

# Python 3 style using string format
print("Age is {0:2d}".format(age))
print("PI = {0:.3f}".format(math.pi))
print("{0} : {1}".format(name, age))
print("{0:*^11} :{1:<20}".format(name, age))

# with f-strings and variable interpolation
print(f"{name} is: {age} years old")
