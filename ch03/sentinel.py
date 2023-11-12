
def main():
    ch = input("Please insert a char: ")

    while ch != '#':
        print(ch, ":", ord(ch))
        ch = input("Please insert a char: ")
    
    print("Goodbye")

if __name__ == "__main__":
    main()