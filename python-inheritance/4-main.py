from 3-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(BaseGeometry):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

if __name__ == "__main__":
    # Create instances of the derived classes
    rectangle = Rectangle(5, 4)
    square = Square(3)

    # Calculate and print areas
    print("Rectangle area:", rectangle.area())
    print("Square area:", square.area())

    # Calling the area() method on the BaseGeometry directly will raise an Exception
    try:
        base = BaseGeometry()
        base.area()
    except Exception as e:
        print("Exception:", e)

