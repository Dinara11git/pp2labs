# if_statement.py
# Примеры простого if

a = 33
b = 200

# Example 1: простое if
if b > a:
    print("b is greater than a")

# Example 2: вложенный if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
