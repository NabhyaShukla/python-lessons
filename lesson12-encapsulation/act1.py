class Student:
    # __init__(), __length__(), __getitem__(), __str__() etc. are functions
    def __init__(self, name, age, pocketmoney):
        self.name = name 
        #private attributes 
        self.__age = age
        self.__pocketmoney= pocketmoney
    
s1 = Student("Nabhya", "12", "$50")
print(s1.name)
print(s1.__age)
print(s1.__pocketmoney)
