# boolean_operators.py
# Примеры логических операторов: and, or, not

a = True
b = False

# Оператор AND
print("Example 1: AND")
print(a and b)  # False
print(a and True)  # True

# Оператор OR
print("Example 2: OR")
print(a or b)  # True
print(b or False)  # False

# Оператор NOT
print("Example 3: NOT")
print(not a)  # False
print(not b)  # True

# Использование логических операторов в условных выражениях
print("Example 4:")
if a and not b:
    print("a истинно и b ложно")
else:
    print("Условие не выполнено")

# Пример с числовыми сравнениями и логикой
x = 15
y = 20
z = 10

print("Example 5:")
if (x > y) or (z < y):
    print("Одно из условий истинно")
else:
    print("Оба условия ложны")
