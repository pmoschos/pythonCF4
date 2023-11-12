# map, filter and lambda

cities = ["london", "paris", "barcelona", "athens", "Casablanka"]

cap_length_cities = list(map(lambda city: city.title(),
                             filter(lambda city: len(city) > 5, cities)))

print(cap_length_cities) 