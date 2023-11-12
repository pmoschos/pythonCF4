f = open('cf2023.txt')

print("Filename:", f.name)
print("Closed:", f.closed)
print("Opening mode:", f.mode)
print("Contents:", f.read())

f.close()