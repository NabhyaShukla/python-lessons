class Student:
    # __init__(), __length__(), __getitem__(), __str__() etc. are functions
    def __init__(self, name, age, pocketmoney):
        self.name = name 
        #private attributes 
        self.__age = age
        self.__pocketmoney= pocketmoney
        #getters and setters
        #getter : fetch the value
    def getAge(self):
            return self.__age #getter only returns
    def getPocketMoney(self):
            return self.__pocketmoney
        #setter : update/modify/change the value
    def setAge(self, age):
            self.__age = age
    def setPocketMoney(self, pocketmoney):
            self.__pocketmoney = pocketmoney
            
s1 = Student("Nabhya", "12", "$50")
print("="*55)
print("Welcome to Student's Record Management...")
print("="*55)
def displayDetails():
    print(f"{s1.name}, {s1.getAge()}, {s1.getPocketMoney()}")

print("\nDo you want to check existing student records(yes/no)")
interest = input().strip().lower()

if interest not in ["yes", "y", "yeah", "yup", "ye", "sure"]:
    exit()
else:
    displayDetails()

    while True:
        print("Do you want to update records? (yes/no)")
        choice = input()
        if choice not in ["yes", "y", "yeah", "yup", "ye", "sure"]:
            print("Good Bye, Human")
            exit()
        else:
            newAge = int(input("Enter New Age: "))
            newPocketMoney = int(input("Enter New Pocketmoney: "))
            s1.setAge(newAge)
            s1.setPocketMoney(newPocketMoney)
            displayDetails()