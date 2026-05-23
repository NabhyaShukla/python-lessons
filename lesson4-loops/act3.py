# Calculate sum of n natural numbers
limit = int(input("Enter a limit : "))
total = 0
i = 1
while i <= limit:
    total = total + i 
    i = i + 1

print(f"The sum of natural numbers upto {limit} is : {total}")