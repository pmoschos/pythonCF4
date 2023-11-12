# regular exp module
import re

stack = []
num = 0

def push(list, item):
    list.append(item)

def pop(list):
    if list:
        return list.pop()
    else:
        print("Stack is emty")

def print_menu():
    print("1. Insert on top")
    print("2. Get from top")
    print("3. q\Q for Quit")

def get_choice():
    return input("Please provide a choice\n")

def main():
    choice = 0
    num = 0
    out_num = 0

    while True:
        print_menu()
        choice = get_choice()

        if not choice:
            continue

        # if choice in ['q', 'Q']
        if choice == 'q' or choice == 'Q':
            break

        pattern = r'^\d$'
        valid = re.match(pattern, choice)

        if not valid:
            print("Error in choice")
            continue

        choice = int(choice)

        match choice:
            case 1:
                num = input("Please insert a number")
                pattern = r'^\d+$'
                valid = re.match(pattern, num)

                if not valid:
                    print("Error")
                    continue

                num = int(num)
                push(stack, num)
                print(str(num) +"inserted")
            
            case 2:
                out_num = pop(stack)
                print("You got:", out_num)
            case _:
                print("Not valid choice")

if __name__ == "__main__":
    main()