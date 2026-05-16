name = "Nabhya"
age = 12
isStudent = True
weight = 41

print("Name :", name)
print("Datatype of name is ", type(name).__name__)

print("Age :", age)
print("Datatype of age is ", type(age).__name__)

print("Is Student :", isStudent)
print("Datatype of isStudent is ", type(isStudent).__name__)

print("Weight :", weight)
print("Datatype of Weight is ", type(weight).__name__)

# Typecasting

age = str(age)
print("Datatype of Age after typecasting is :", type(age).__name__)

weight = float(weight)
print("Datatype of Weight after typecasting is :", type(weight).__name__)
print("Value of weight after typecasting is :", weight)
