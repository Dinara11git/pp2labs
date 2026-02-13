# while_loop.py
# Примеры обычного while цикла

i = 1

# Example 1: простой while
while i < 6:
    print(i)
    i += 1

# Example 2: while с условием выхода
i = 1
while i < 6:
    print(i)
    i += 1

# Example 3: while с вложенным if
i = 1
while i < 6:
    print(i)
    if i == 3:
        print("i is 3")
    i += 1

# Example 4: while с else
i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("i is no longer less than 4")

# Example 5: while с break внутри
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
