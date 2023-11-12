# password generator
import string
import random

characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_password():
    password_length = int(input("Give the password length: "))
    random.shuffle(characters)
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    password = "".join(password)
    print(password)

def main():
    while True:
        option = input("Do you want to create a password? ('y' or 'q' for quit)")

        if option.lower() == 'y':
            generate_password()
        elif option.lower() == 'q':
            print("Goodbye")
            break
        else:
            print("Wrong input")

if __name__ == "__main__":
    main()