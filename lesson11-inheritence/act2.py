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
    def __init__(self, name, money, watch, laptop, ):
        Grandpa.__init__(self, name, money, watch)
        self.laptop = laptop

    def displayAssets(self):
        return Grandpa.displayAssets(self) + f" and also {self.laptop}"
    
gs1 = Grandson("Nabhya", "100,000", "Rolex", "HP Omnibook")
gs2 = Grandson("Viaan", "100,000", "Rolex", "HP Pavillion")

print(gs1.displayAssets())
print(gs2.displayAssets())