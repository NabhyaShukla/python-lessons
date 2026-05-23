# within a  range print all the prime numbers
lower = int(input("Enter Lower Range : "))
upper = int(input("Enter Upper Range : "))

print(f"Total prime numbers within {lower} and {upper} are : ")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % 2 != 0:
                print(num, "is a prime number")
                break
        else:
            print(num)