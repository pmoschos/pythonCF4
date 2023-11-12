def main():
    n = int(input("Please insert an int: "))
    a, b = 0, 1

    for i in range(2, n + 1):
        a, b = b, a + b

    print(b)

if __name__ == "__main__":
    main()