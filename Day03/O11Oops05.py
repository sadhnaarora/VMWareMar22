
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized......")

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")

ply1 = Player("Sachin", 35)
ply1.get_details()

print("-" * 40)
ply2 = Player('Sourav', 34)
ply2.get_details()

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")
ply2.runs = 150

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")
