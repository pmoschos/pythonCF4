
def main():
    ch = input("Please insert a char: ")

    while True:
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
        if ch == '#': break
    
    print("Goodbye")

if __name__ == "__main__":
    main()