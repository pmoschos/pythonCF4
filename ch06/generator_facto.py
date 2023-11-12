def facto():
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

f = facto()

for i in range(6):
    print(f"{i}! = {next(f)}")


for i in range(6, 11):
    print(f"{i}! = {next(f)}")