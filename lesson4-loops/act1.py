#printing a number table 

num = int(input("Enter a number to multiply : "))

for i in range(1, 11): # Print multiplication table in limited loops (10 times)
    print(f"{num} x {i} = {num * i}") #f"---" f is for printing the input value by the user

numAdd = int(input("Enter a number to add : "))
for i in range(1, 11): # Print addition table in limited loops (10 times)
    print(f"{numAdd} + {i} = {numAdd + i}") #f"---" f is for printing the input value by the user