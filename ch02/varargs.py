# print cities
def print_cities(*cities):
    for city in cities:
        print(city, end=" ")
    print()

def main():
    print_cities("Athens", "Paris", "London")
    print_cities("London")

if __name__ == "__main__":
    main()

