# while_continue.py
# Corrected examples of while loops with continue
# Safe for execution without infinite loops

# Example 1: simple continue
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # skip printing 3
    print(i)

print("---- Example 1 done ----\n")

# Example 2: continue with multiple conditions
i = 0
while i < 6:
    i += 1
    if i == 2 or i == 4:
        continue  # skip printing 2 and 4
    print(i)

print("---- Example 2 done ----\n")

# Example 3: combine continue and break
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue  # skip 3
    if i == 5:
        break     # stop loop at 5
    print(i)

print("---- Example 3 done ----\n")

# Example 4: nested while loops with continue (safe)
i = 0
while i < 3:
    j = 0
    while j < 3:
        j += 1
        if j == 2:
            continue  # skip printing 2
        print(f"i={i}, j={j}")
    i += 1  # increment outer loop

print("---- Example 4 done ----\n")

# Example 5: while loop with else
i = 0
while i < 2:
    i += 1
    print(i)
else:
    print("i is no longer less than 2")

print("---- Example 5 done ----\n")
