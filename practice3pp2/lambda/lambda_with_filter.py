"""
Using lambda with filter()
"""

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

is_even = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", is_even)
