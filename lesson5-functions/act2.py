# factorial using function recursion

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)
try:
    num = int(input("Enter a number to check its factorial : "))

    if num < 0:
        print("Invalid Input")
    else:
        print(f"The factorial of {num} is {factorial(num)}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
