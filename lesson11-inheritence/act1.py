#parent class
class Grandpa:
    def __init__(self, name, money, watch):
        self.name = name
        self.money = money
        self.watch = watch

    def displayAssets(self):
        return f"{self.name} has ${self.money} and a {self.watch} watch"
    
#child class
class Grandson(Grandpa):
    pass

#create an object of Grandpa
g1 = Grandpa("Mr. Ashok K. Shukla", "100,000", "Rolex")
print(g1.displayAssets)