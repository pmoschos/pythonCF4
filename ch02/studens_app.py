# class def
class Student:
    """
    A class that represents a person with firstname and lastname
    
    Attributes:
    - firstname (str) : the firstname of the person
    - lastname (str) : the last name of the person
    """
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

def main():
    p = Student("Bob", "M")
    print(p.firstname)
    print(p.lastname)

if __name__ == "__main__":
    main()