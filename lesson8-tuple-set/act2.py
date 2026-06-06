# All about set
# create a set

prime_numbers = {2, 3, 5, 7, 7, 3}
print(prime_numbers) # set does not allow duplicate values

print("\n")
print("*" * 50)
print("\n")

# copying set
# shallow copy
prime_copy = prime_numbers.copy()
print(f"Original Set : {prime_numbers}")
print(f"Original Set : {prime_copy}")

print("\n")
print("*" * 50)
print("\n")

# equality
print(prime_numbers == prime_copy) # checks if the values in both sets are the same
print(prime_numbers is prime_copy) # 'is' is a comparison operator that checks if both variables point to the same object in memory

print("\n")
print("*" * 50)
print("\n")

# Adding $ Removing
prime_numbers.add(11)
prime_numbers.add(7)
print(f"After Adding new elements : {prime_numbers}")

print("\n")
print("*" * 50)
print("\n")

# Removing
# 1. Discard : Safe Removal
prime_numbers.discard(7)
prime_numbers.discard(10)
print(f"After removal : {prime_numbers}")

print("\n")

# 2. Remove : Raise Exception
item_to_remove = 100
try:
    print("Trying To remove '100' from SET..." )
    prime_numbers.remove(100)
    print("Successfully removed")
except KeyError:
    print(f"{item_to_remove} not found...")
finally:
    print("Program Ends...")

try:
    print("Trying To remove '100' from SET..." )
    prime_numbers.remove(5)
    print("Successfully removed")
except KeyError:
    print(f"{item_to_remove} not found...")
finally:
    print("Program Ends...")

print("\n")

# 3. pop()
popped_val = prime_numbers.pop()
print(f"Item removed : {popped_val}")
print(f"After Item removal : {prime_numbers}")

print("\n")
print("*" * 50)
print("\n")

# 
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# union() = returns a new set that contains all the elements from both sets
print(set1.union(set2))

# intersection() = returns a new set that contains only the elements that are common to both sets
print(set1.intersection(set2))

# difference() = returns a new set that contains only the elements that are in the first set but not in the second set
print(set1.difference(set2))
print(set2.difference(set1))

# Symmetric Difference() = returns a new set that contains only the elements that are in either of the sets but not in both sets
print(set1.symmetric_difference(set2))
print(set2.symmetric_difference(set1))

# issubset, issuperset, disjoint
print({1, 2}.issubset(set1))
print({1, 2, 3, 4, 5, 6}.issuperset(set1))
print({1, 2}.isdisjoint({3, 4}))

# clear
set1.clear()

# del
del set1