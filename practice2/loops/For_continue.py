# for_continue.py
# Примеры for цикла с continue

fruits = ["apple", "banana", "cherry"]

# Example 1: пропуск элемента
for x in fruits:
    if x == "banana":
        continue
    print(x)

# Example 2: continue с range()
for x in range(6):
    if x == 3:
        continue
    print(x)

# Example 3: несколько условий
for x in range(1, 10):
    if x % 2 == 0:
        continue
    print(x, "is odd")

# Example 4: continue в вложенном цикле
colors = ["red", "green", "blue"]
for color in colors:
    for fruit in fruits:
        if fruit == "banana":
            continue
        print(color, fruit)

# Example 5: комбинирование break и continue
for x in range(6):
    if x == 2:
        continue
    if x == 5:
        break
    print(x)
