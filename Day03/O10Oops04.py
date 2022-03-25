
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 35

    def get_details(self):
        print(f"Name :{self.name}\nAge :{self.age}")


ply1 = Player()
ply1.get_details()

print("-" * 30)
ply2 = Player()
ply2.name = "Rahul"
ply2.age = 33

print(f"Name :{ply2.name}")
print(f"Age  :{ply2.age}")
