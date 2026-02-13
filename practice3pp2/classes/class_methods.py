"""
Example of instance methods and working with objects
"""

import math

class Point:
    """Represents a point in 2D space"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        """Displays coordinates"""
        print(f"Point: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        """Moves point to new coordinates"""
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        """Returns distance to another point"""
        return math.sqrt((self.x - other_point.x)**2 +
                         (self.y - other_point.y)**2)


if __name__ == "__main__":
    p1 = Point(4, 9)
    p2 = Point(10, 5)

    p1.show()
    print("Distance:", p1.dist(p2))
