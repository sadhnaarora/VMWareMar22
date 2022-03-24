
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'a': 1, 'b': 2, 30: 3 }
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([("name", "sachin"), ("runs", 125), ('oppo', 'NZL'), ('venue', 'auckland')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Rahul", age=34, runs=85, oppo='PAK', year=2001)
d4['gender'] = "Male"
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'virat', 'runs': 150, 'oppn': 'SA', 'vunue': 'Chepauk','age': 30}
print(f"player :{player}")
print(type(player))

# new pair
player['year'] =  2018

# modify the value
player['oppn'] =  "Sri Lanka"

# del key
del player['age']

# key with null value
player['RR'] = None

print(f"player :{player}")

print("-" * 40)
# print(player['age'])

print(player.get('age'))

print(player.get('age', "Invalid Key, Please enter a valid key"))

print(player.get('name', "Invalid Key, Please enter a valid key"))

print("-" * 40)
print(dir(player))
