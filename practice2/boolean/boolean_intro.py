# boolean_intro.py
# Примеры простых булевых значений

# True и False
print("Example 1:")
print(True)
print(False)

# Присваивание переменных
a = True
b = False
print("Example 2:")
print(a)
print(b)

# Булевы значения от выражений
print("Example 3:")
print(10 > 9)   # True
print(10 < 9)   # False

# Булевы значения от пустых и непустых объектов
print("Example 4:")
print(bool("Hello"))      # True
print(bool(""))           # False
print(bool([1, 2, 3]))   # True
print(bool([]))           # False
