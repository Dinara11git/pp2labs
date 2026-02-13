"""
Basic class definition example
"""

class InputOutString:
    """Class that stores and prints a string in uppercase"""

    def __init__(self, text=""):
        self.s = text

    def get_string(self, text):
        """Stores a string"""
        self.s = text

    def print_string(self):
        """Prints the string in uppercase"""
        print(self.s.upper())


# Example usage
if __name__ == "__main__":
    obj = InputOutString()
    obj.get_string("hello world")
    obj.print_string()
