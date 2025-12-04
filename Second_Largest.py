arr = [10, 5, 20, 8, 12]
n = len(arr)

largest = arr[0]
slargest = -1  

for i in range(n):
    if arr[i] > largest:
        slargest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i] > slargest:
        slargest = arr[i]

print("Second largest element:", slargest)
