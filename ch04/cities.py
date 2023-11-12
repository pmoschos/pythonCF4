# map and lambda

cities = ["london", "paris", "barcelona", "athens"]

cap_cities = list(map(lambda city: city.title(), cities))

print(cap_cities)