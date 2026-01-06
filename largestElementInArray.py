arr = [4, 7, 1, 9, 3]
largest = arr[0]

for i in range(1, len(arr)):
    if arr[i] > largest:
        largest = arr[i]

print(largest)
