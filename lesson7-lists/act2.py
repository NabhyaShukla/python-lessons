# Python object 
# obj = {key:value pair}      {{{{{!!IMPORTANT!!}}}}}
# Dictionary is same as an object but is used in python

# Creating a dictionary
teacher = {
    "name" : "Mr. Deb",
    "subject" : "coding langs",
    "experience" : "10 years",
}

print(f"Teacher's Profile : {teacher}")

# Perform dictionary operations
# access some value using key
print(f"{teacher['name']} teaches {teacher['subject']}")
print("-" * 116)
teacher['experience'] = "11 years"
teacher['email'] = "mr.deb@rediff.com"

# pop
teacher.pop('experience')
print(f"Updated Teacher's Profile : {teacher}")

# get
print(f"Teacher's Email : {teacher.get('email', 'Email not found')}")
print("-" * 116)
