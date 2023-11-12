# meaning of else in for loop

sales = ["apples", "oranges", "bananas", "eggs"]

print("eggs" not in sales)

for item in sales:
    if "eggs" in sales:
        print(item)
    else:
        break
else:
    print("Come to eat")