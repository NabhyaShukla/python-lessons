# A simple calc 
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y



print("Greetings, user! Welcome to this SIMPLE CALCULATOR!")
print(" ")
print("*" * 101)
print(" ")

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second Number : "))
print(" ")
print("*" * 101)
print(" ")

print("Enter Your Choice : ")
print("\n Enter '1' for ADDITION")
print("Enter '2' for SUBTRACTION")
print("Enter '3' for MULTIPLICATION")
print("Enter '4' for DIVISION")
choice = int(input("What do you want perform? : "))

if choice == 1:
    print(f"The result addition of {num1} and {num2} is : {add(num1,num2)}")
elif choice == 2:
    print(f"The result subtraction of {num1} and {num2} is : {subtract(num1,num2)}")
elif choice == 3:
    print(f"The result multiplication of {num1} and {num2} is : {multiply(num1,num2)}")
elif choice == 4:
    print(f"The result division of {num1} and {num2} is : {divide(num1,num2)}")
else:
    print("Invalid choice! Please select a valid option.")