from functools import reduce

quarters = ['A', 'B', 'C', 'D']
prices = [1000, 2000, 1800, 1500]

# create sales dict
sales = dict(zip(quarters, prices))
print("sales:", sales)

print("-------------------")
for key, value in sales.items():
    print(key, ":", value)

filtered_sales = dict(filter(lambda quarter_tumple: quarter_tumple[1] >= 1500,
                      sales.items()))
print("filtered_sales:", filtered_sales)

# taxes
quarters_tax = {key : value * 0.2 for key, value in sales.items()}
print("quarters_tax:", quarters_tax)

# count total sales
total_year_sales = reduce(lambda x, y: x + y, sales.values())
print("total_year_sales:", total_year_sales)

# 2nd way to count total sales
print(sum(sales.values()))