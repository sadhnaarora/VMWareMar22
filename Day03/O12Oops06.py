
class Player:
    team = "India"          # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized......")

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

ply1 = Player("Dhoni", 32)
ply2 = Player("Yuvraj", 33)

ply1.get_details()
ply2.get_details()
print("-" * 40)

print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "CSK"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

ply2.team = "Kings XI Punjab"

print("-" * 40)
print(f"ply2   :{ply2.team}")
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

print("-" * 40)
print(Player.__dict__)
