class Point:
    __count = 0

    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y
        Point.__count += 1
    
    @classmethod
    def getCount(cls):
        return cls.__count

    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, y):
        self.__y = y


def main():
    p = Point(10, 20)
    print(p.x, p.y)
    p.x = 100
    p.y = 200
    print(p.x, p.y)
    p2 = Point(14, 18)

    print("Number of points:", Point.getCount())

if __name__ == "__main__":
    main()