# Function recursion = calling a function inside the same function
def greetMe(first_name, last_name, greet="Hi"):
    full_name = first_name + " " + last_name
    print(f"{greet}, {full_name}")  #The output is according to the input of the user and the default value of greet
    

first_name = input("What is your first name? : ")
last_name = input("What is your last name? : ")

greetMe(first_name, last_name, "Greetings")
greetMe(first_name, last_name)