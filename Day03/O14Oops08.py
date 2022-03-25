
# magic methods
class Player:

    def __init__(self, name, age):
        print("Init....")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name :{self.name}\nAge :{self.age}"

ply1 = Player("Sachin",  38)

print("-" * 40)
print(str(ply1))

print("-" * 40)
print(ply1)                 # implicitly calls __str__
