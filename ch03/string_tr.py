def name_spacing(num):
    name = input("Please give a name: ")

    for char in name:
        print(char, end=' ' * num)

name_spacing(3)