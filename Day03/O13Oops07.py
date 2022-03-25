
class Player:

    def __init__(self, name, age):
        print("Init....")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):           # factory
        return cls(f"Mr. {fname} {lname}", age)          #pass

ply1 = Player("Sachin",  38)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Mahendar", "Dhoni", 32)
ply2.get_details()

