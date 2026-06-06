# All about Tuple

# Create tuple "pasta" and "biryani"
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Veg Biryani", "Indian", 45, "Hard")

# display values
print("Recipe 1 : ", pasta)
print("Name of Recipe 1 : ", pasta[0])
print("Cuisine of Recipe 1 : ", pasta[1])
print(f"Prep Time of Recipe 1 :{pasta[2]} minutes")
print("Difficulty of Recipe 1 : ", pasta[-1])

print("\n")
print("*" * 50)
print("\n")

# tuple slicing
# combine two tuples ==> nested tuple
all_tuples = (pasta, biryani)
print(f"First Recipe Name : {all_tuples[0][0]}")
print(f"Second Recipe Name : {all_tuples[1][0]}")
print(f"Second Recipe Prep-Time : {all_tuples[1][2]} minutes")
print(f"Second Recipe Difficulty Level : {all_tuples[1][3]}")

print("\n")
print("*" * 50)
print("\n")

# iterate through a tuple (loops through a tuple)
print("Iterate/Loop through a Tuple")
for detail in pasta:
    print("-", detail)

print("\n")
print("*" * 50)
print("\n")

# Enumerate() = adds a counter to an iterable and returns it in a form of enumerate object
print("Enumerate through a tuple")
for index, detail in enumerate(biryani, start=1):
    print(f"{index} : {detail}")

print("\n")
print("*" * 50)
print("\n")

# Tuple Unpacking = assigning values from a tuple to variables
fruits = ("apple", "banana", "kiwi", "orange", "apple")
f1, f2, f3, f4, f5 = fruits
print(f1)
print(f2)
print(f3)
print(f4)
print(f5)

print("\n")
print("*" * 50)
print("\n")

x, *y = fruits
print(x)
print(y)

print("\n")
print("*" * 50)
print("\n")

# index() = returns the index of the first occurrence of a value in a tuple
print(fruits.index("apple"))

print("\n")
print("*" * 50)
print("\n")

# count() = returns the number of times a value appears in a tuple
print(fruits.count("apple"))

print("\n")
print("*" * 50)
print("\n")

# in/not in operator = checks if a value exists in a tuple and returns True or False
print("apple" in fruits)
print("apple" not in fruits)

# zip() = combines two or more iterables (like lists, tuples) into a single iterable of tuples
t1 = (1, 2, 3)
t2 = ("John", "David", "Mayank")

t3 = dict(zip(t1, t2))
print(t3)

print("\n")
print("*" * 50)
print("\n")

# gives clean output without curly braces and quotes
for id, name in t3.items():
    print(f"{id} : {name}")