import random
import math

def main():
    secret = random.randint(1, 10)
    tries = 0
    MAX_TRIES = 5

    while True:
        if tries == MAX_TRIES: break

        num = int(input("Please insert an int: "))

        if num == secret:
            print("Bingo! Secret numner:", secret)
            break
        elif math.fabs(num - secret) <= 5:
            print("Hot")
        else:
            print("Cold")
        
        tries += 1
        
    if tries == MAX_TRIES:
        print("You reached the max number of tries:", MAX_TRIES)

if __name__ == "__main__":
    main()