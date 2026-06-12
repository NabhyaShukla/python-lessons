class Student:
    # Methods

    # Inbuilt to initialize objects
    def __init__(self, name, grade , school, country, state , subject):
        self.name = name
        self.grade = grade
        self.school = school
        self.country = country
        self.state = state
        self.subject = subject

    def intro(self):
        print(f"I am {self.name}, live in {self.state}, {self.country} and I am in {self.grade} grade.")

    def education(self):
        print(f"I go to {self.school} institute, and I study {self.subject}")

Viaan = Student("Viaan", "7th", "Codingal", "INDIA", "Uttarakhand", "Python")
Nabhya = Student("Nabhya", "7th", "Codingal", "U.S.A.", "Colorado", "Python")

Viaan.intro()
Nabhya.intro()

print("*" * 59)

Viaan.education()
Nabhya.education()
