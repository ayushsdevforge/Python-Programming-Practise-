arr = [1, 2, 3, 4]
sorted_flag = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_flag = False
        break

print(sorted_flag)
