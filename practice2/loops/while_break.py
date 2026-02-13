# while_break.py
# Примеры while цикла с break

i = 1

# Example 1: простой break
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1

# Example 2: break с вложенным условием
i = 0
while i < 6:
    i += 1
    if i == 4:
        break
    print(i)

# Example 3: break с continue в том же цикле
i = 0
while i < 6:
    i += 1
    if i == 3:
        break
    print(i)

# Example 4: while с break и else
i = 0
while i < 5:
    print(i)
    if i == 2:
        break
    i += 1
else:
    print("Finished without break")

# Example 5: while с несколькими break
i = 0
while i < 10:
    i += 1
    if i == 3:
        break
    print(i)
