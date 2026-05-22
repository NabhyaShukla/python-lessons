# whether the number is greater than 100 or not
# if it is greater than 100 then check whether it is odd or even

# THIS IS NESTED IF STATEMENT!
num = int(input("Enter a Number to check : "))
if num > 100 : 
    print(f"{num} is greater than 100!")
    if num % 2 == 0:
        print(f"{num} is even too!")
    else:
        print(f"{num} is odd too!")
else:
    print(f"{num} is less than 100!")
