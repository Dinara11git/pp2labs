"""
Using super() in inheritance
"""

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")


class Student(Person):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, GPA: {self.gpa}")


if __name__ == "__main__":
    s = Student("Dinara", 3.8)
    s.greet()
    s.display()
