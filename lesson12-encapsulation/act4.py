class Cricket:
    def __init__(self, player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Cricket - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} hits a SIX!")
    
    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score > 0:
            self.__score = new_score
            print(f"Score updated to {self.__score}")
        else:
            print(f"Score can't be negative.")

class Football:
    def __init__(self,player, score):
        self.__player = player
        self.__score = score

    def info(self):
        print(f"Football - Player: {self.__player}, Score: {self.__score}")

    def play(self):
        print(f"{self.__player} scores a goal!")

    def get_score(self):
        return self.__score
    
    def set_score(self, new_score):
        if new_score > 0:
            self.__score = new_score
            print(f"Score updated tp {self.__score}")
        else:
            print("Score Can't be neggative.")

#Create opjects
cricket = Cricket("Rohit Sharma", 176)
football = Football("Sunil Chhetri", 3)

#Polymorphism - same method, different behaviour
print("=== Sports Scoreboard ===\n")
for sports in (cricket, football):
    sports.info()
    sports.play()
    print()

#Encapsulation - direct change doesnt NOT work
print("--- Direct change attempt---")
cricket.__score = 999
print(f"get_score() still shows : {cricket.get_score()}")

#setter - the only safeway to update
print("\n--- Updating Scores ---")
cricket.set_score(200)
football.set_score(4)