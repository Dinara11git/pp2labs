"""
Example of class variables vs instance variables
"""

class Student:
    school_name = "PP2 University"   # Class variable

    def __init__(self, name):
        self.name = name              # Instance variable

    def display(self):
        print(f"Name: {self.name}, School: {Student.school_name}")


if __name__ == "__main__":
    s1 = Student("Dinara")
    s2 = Student("Ali")

    s1.display()
    s2.display()

    # Change class variable
    Student.school_name = "New University"

    s1.display()
    s2.display()
