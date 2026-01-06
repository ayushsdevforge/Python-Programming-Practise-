arr = [10, 20, 5, 8, 50]

largest = second = -1

for i in arr:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print(second)
