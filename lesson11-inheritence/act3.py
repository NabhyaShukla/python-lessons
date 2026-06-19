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
        super().__init__(name, money, watch)
        self.laptop = laptop

    def displayAssets(self):
        return super().displayAssets() + f" and also {self.laptop}"
    
gs1 = Grandson("Nabhya", "1,100,000", "Titan", "Apple Macbook")
gs2 = Grandson("Viaan", "1,100,000", "Titan", "Yapple Mahakbook i")

print(gs1.displayAssets())
print(gs2.displayAssets())
