# short_hand_if.py
# Короткая форма if-else (тернарный оператор)

a = 2
b = 330

# Example 1
print("A") if a > b else print("B")

# Example 2: тернарный оператор с elif
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
