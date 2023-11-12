bag1 = {"A1", "A2", "A3", "A4", "BA1"}
bag2 = {"A1", "A2", "B3", "B4", "BB2"}

common_elemnts = bag1 & bag2
common_elemnts = bag1.intersection(bag2)
print("common_elemnts of bag1 and bag2:", common_elemnts)

all_the_elements = bag1 | bag2
all_the_elements = bag1.union(bag2)
print("all_the_elements of bag1 and bag2:", all_the_elements)

diff1 = bag1 - bag2
diff1 = bag1.difference(bag2)
print("diff1 of bag1 and bag2:", diff1)

diff2 = bag1 ^ bag2
diff2 = bag1.symmetric_difference(bag2)
print("diff2 of bag1 and bag2:", diff2)