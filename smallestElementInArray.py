arr = [3,4,5,11,1,2]

smallest = arr[0]

for i in arr: 
    if i < smallest:
        smallest = i
        print(smallest)
print("Smallest element is:", smallest)