arr=[10,20,4]

for i in range(0, len(arr)):
    if i == 0:
        maxElement = arr[i]
    if arr[i] > maxElement:
        maxElement = arr[i]
print(maxElement)

for i in range(0, len(arr)):
    if i == 0:
        minElement = arr[i]
    if arr[i] < minElement:
        minElement = arr[i]
print(minElement)