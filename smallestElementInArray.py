arr = [4, 7, 1, 9, 3]
smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)
