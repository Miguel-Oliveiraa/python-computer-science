num = 5
result = 1

# Loop statement approach
if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("The Factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        result *= i
    print("The factorial of", num, "is", result)