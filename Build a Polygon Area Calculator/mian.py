class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for _ in range(self.height):
            picture += "*" * self.width + "\n"
        return picture

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def __str__(self):
        return f"Square(side={self.width})"


# Demonstration and tests

# Usage example
print("Usage Example:")
rect = Rectangle(10, 5)
print(rect.get_area())  # 50
rect.set_height(3)
print(rect.get_perimeter())  # 26
print(rect)  # Rectangle(width=10, height=3)
print(rect.get_picture())  # 3 lines of 10 stars

sq = Square(9)
print(sq.get_area())  # 81
sq.set_side(4)
print(sq.get_diagonal())  # 4*sqrt(2) ≈ 5.6569
print(sq)  # Square(side=4)
print(sq.get_picture())  # 4 lines of 4 stars

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # 8

# Automated Tests
print("\nAutomated Tests:")
from math import isclose

# 1 & 3. Subclass and isinstance checks
print("1 & 3:", issubclass(Square, Rectangle), isinstance(Square(2), Rectangle), isinstance(Square(2), Square))

# 4 & 5. __str__
print("4:", str(Rectangle(3, 6)) == "Rectangle(width=3, height=6)")
print("5:", str(Square(5)) == "Square(side=5)")

# 6 & 7. get_area
print("6:", Rectangle(3, 6).get_area() == 18)
print("7:", Square(5).get_area() == 25)

# 8 & 9. get_perimeter
print("8:", Rectangle(3, 6).get_perimeter() == 18)
print("9:", Square(5).get_perimeter() == 20)

# 10 & 11. get_diagonal
print("10:", isclose(Rectangle(3, 6).get_diagonal(), 6.708203932499369))
print("11:", isclose(Square(5).get_diagonal(), 7.0710678118654755))

# 12. Rectangle __str__ after setting new values
r = Rectangle(3, 6)
r.set_width(7)
r.set_height(8)
print("12:", str(r) == "Rectangle(width=7, height=8)")

# 13 & 14. Square __str__ after set_side and set_width/set_height
s = Square(5)
s.set_side(9)
print("13:", str(s) == "Square(side=9)")
s.set_width(3)
print("14:", str(s) == "Square(side=3)")
s.set_height(4)
print("14 (height):", str(s) == "Square(side=4)")

# 15 & 16 & 17. get_picture
r_pic = Rectangle(2, 3).get_picture()
print("15:", r_pic == "**\n**\n**\n")
s_pic = Square(2).get_picture()
print("16:", s_pic == "**\n**\n")
big_pic = Rectangle(51, 1).get_picture()
print("17:", big_pic == "Too big for picture.")

# 18, 19, 20. get_amount_inside
print("18:", Rectangle(15, 10).get_amount_inside(Square(5)) == 6)
print("19:", Rectangle(4, 8).get_amount_inside(Rectangle(3, 6)) == 1)
print("20:", Rectangle(2, 3).get_amount_inside(Rectangle(3, 6)) == 0)