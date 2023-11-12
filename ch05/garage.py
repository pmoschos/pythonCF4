from collections import deque

# create a deque
garage = deque()

# simulate some cars arriving in the garage
garage.append("Car 1")
garage.append("Car 2")
garage.append("Car 3")
garage.append("Car 4")

# simulate a car leaving the garage (FIFO)
car_left = garage.popleft()

# simulate some cars arriving in the garage
garage.append("Car 5")
garage.append("Car 6")

print("Current satat of the garage:", list(garage))
print("Last car which left from the garage", car_left)