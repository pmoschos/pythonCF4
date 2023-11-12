def main():
    facto = 1
    n = int(input("Please insert an int: "))

    for i in range(1, n + 1):
        facto *= i
    
    print(f"{n}! = {facto:,}")

    pass

if __name__ == "__main__":
    main()