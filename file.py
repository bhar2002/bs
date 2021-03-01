def factorial(n):
    if n == 1:
        return n
    return n* factorial(n-1)



print(factorial(8))
print( factorial(10))

num = int(input("enter number to calculate factorial"))

print (factorial(num))

