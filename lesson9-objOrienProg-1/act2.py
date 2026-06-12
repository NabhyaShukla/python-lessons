class Student:
    # PROPERTIES
    grade = "8th"
    school = "Codingal"
    country = "Netherlands"
    subject = "Python"

    # Method
    def intro(self):
        print(f"I live in {self.country} and I am in {self.grade} grade")

    def education(self):
        print(f"I go to {self.school} institute, and I study {self.subject}")

Viaan = Student()
Nabhya = Student()

Viaan.intro()
Nabhya.intro()

print("*" * 59)

Viaan.education()
Nabhya.education()