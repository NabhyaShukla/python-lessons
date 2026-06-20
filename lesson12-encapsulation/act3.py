class Student:
    def __init__(self, name, town, pin):
        self.name = name
        self.town = town
        self.pin = pin
    #private method in python class
    def __displayDetails(self):
        print(f"{self.name}, {self.town}, {self.pin}")

    def display(self):
        self.__displayDetails

s1 = Student("NABHYA", "DIBIYAPUR", "206244")
s1.__displayDetails()
s1.display()