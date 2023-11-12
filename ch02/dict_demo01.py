# dictionary crud functions

products = {1:"apples", 2:"bananas", 10:"honey"}

print(products)

# Insert
products[3] = "oranges"

# Update
products[2] = "milk"

# Delete
del products[1]
print(products)

print("=====")

for key in products.keys():
    print(key, products[key])

print("=====")
for value in products.values():
    print(value)
    
print("=====")

for key, value in products.items():
    print(key, ":", value)