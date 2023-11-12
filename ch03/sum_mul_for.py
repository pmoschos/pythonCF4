
def main():
    sum = 0
    mul = 1

    upper_bound = int(input("Please insert an int: "))

    for i in range(1, upper_bound + 1):
        sum += i
        mul *= i
    
    print(f"Sum (1 - {upper_bound}): {sum:,}")
    print(f"Mul (1 - {upper_bound}): {mul:,}")


if __name__ == "__main__":
    main()