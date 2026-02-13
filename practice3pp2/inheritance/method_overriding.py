"""
Method overriding example
"""

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


if __name__ == "__main__":
    a = Animal()
    d = Dog()

    a.sound()
    d.sound()
