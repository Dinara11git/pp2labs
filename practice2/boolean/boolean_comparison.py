# boolean_comparison.py
# Примеры сравнения значений

x = 10
y = 20

# Примеры сравнения
print("Example 1:")
print(x == y)   # False
print(x != y)   # True
print(x > y)    # False
print(x < y)    # True
print(x >= 10)  # True
print(y <= 20)  # True

# Использование if с булевым выражением
print("Example 2:")
if x < y:
    print("x меньше y")
else:
    print("x не меньше y")

# isinstance проверка
print("Example 3:")
print(isinstance(x, int))   # True
print(isinstance(y, str))   # False
