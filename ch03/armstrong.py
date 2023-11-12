
def main():
    num = int(input("Please insert an int: "))
    is_armstrong = False
    digits_count = 0
    sum = 0

    tmp = num

    while tmp != 0:
        digits_count += 1
        tmp //= 10
    
    tmp = num
    while tmp != 0:
        rightmost_digit = tmp % 10
        sum += rightmost_digit ** digits_count
        tmp //= 10
    
    is_armstrong = (num == sum)
    print(f"{num} is armstrong: {is_armstrong}")


if __name__ == "__main__":
    main()