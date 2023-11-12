def get_average(num1, num2, num3):
    return "{:.2f}".format((num1 + num2 + num3) / 3)

def main():
    n1 = 10
    n2 = 20
    n3 = 15

    average = get_average(n1, n2, n3)
    print(average)

if __name__ == "__main__":
    main()