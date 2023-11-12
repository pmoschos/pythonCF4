def main():
    n = int(input("Please insert an int: "))
    a = 0
    b = 1

    for i in range(2, n + 1):
        temp = a
        a = b
        b = temp + b

    print(b)

if __name__ == "__main__":
    main()