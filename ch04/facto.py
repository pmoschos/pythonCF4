# n! = 1*2*3*..*n
# n! = n * (n-1)!
# 0! = 1, 1! = 1

def facto(n):
    if n < 0: return 0
    if n in (0, 1): return 1
    return n * facto(n - 1)

def main():
    n = 10
    print(f"{n}! = {facto(n):,.2f}")

if __name__ == '__main__':
    main()
