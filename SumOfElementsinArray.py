arr = [1,2,3,4,5]
result = 0

# By me
for i in range(0, len(arr)):
    result += arr[i]
print(result)

# Function sum
print(sum(arr))
print(sum(arr, 10))
print(sum(arr, -10))
