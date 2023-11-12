def fibo(n):
    if n in (0, 1):
        return n
    return fibo(n -1) + fibo(n - 2)

def main():
    n = 7
    print(f"fibo({n}) = {fibo(n):,.2f}")

if __name__ == '__main__':
    main()