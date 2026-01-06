arr = [1, 2, 2, 3, 4, 4]
unique = []

for i in arr:
    found = False
    for j in unique:
        if i == j:
            found = True
            break
    if not found:
        unique.append(i)

print(unique)
