# for_break.py
# Примеры for цикла с break

fruits = ["apple", "banana", "cherry"]

# Example 1: break внутри цикла
for x in fruits:
    print(x)
    if x == "banana":
        break

# Example 2: break перед печатью
for x in fruits:
    if x == "banana":
        break
    print(x)

# Example 3: break с range()
for x in range(6):
    if x == 3:
        break
    print(x)

# Example 4: for ... else с break
for x in range(6):
    if x == 4:
        break
    print(x)
else:
    print("Finished without break")

# Example 5: вложенный for с break
adjectives = ["red", "big"]
for adj in adjectives:
    for fruit in fruits:
        if fruit == "banana":
            break
        print(adj, fruit)
