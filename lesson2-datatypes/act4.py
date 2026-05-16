# Swap a number using temporary variable
num1 = 12
num2 = 30

print("Num1 :", num1)
print("Num2 :", num2)
print("-"*41)

temp = 0
temp = num1
num1 = num2
num2 = temp

print("Num1 after swapping :", num1)
print("Num2 after swapping :", num2)