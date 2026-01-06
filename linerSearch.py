arr = [10, 20, 30, 40]
key = 30
found = False

for i in arr:
    if i == key:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
