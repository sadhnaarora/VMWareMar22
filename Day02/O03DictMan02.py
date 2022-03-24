
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
'pop', 'popitem', 'setdefault', 'update', 'values'
"""

print("keys".center(40,"-"))
player = {'name': 'virat', 'runs': 150, 'oppn': 'SA', 'vunue': 'Chepauk','age': 30}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")
for i in k:
    print(i, end=" ")
print()

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'virat', 'runs': 150, 'oppn': 'SA', 'vunue': 'Chepauk','age': 30}
print(f"player :{player}")

v = player.values()
print(f"v :{v}")
print(type(v))

print("-" * 40)
player = {'name': 'virat', 'runs': 150, 'oppn': 'SA', 'vunue': 'Chepauk','age': 30}
print(f"player :{player}")

for i in player:            # access the keys of the dictionary
    print(i, end=" ")
print()

print("setdefault".center(40,"-"))
player = {'name': 'virat', 'runs': 150, 'oppn': 'SA', 'vunue': 'Chepauk','age': 30}
print(f"player :{player}")

player.setdefault('age', 34)
player.setdefault('team', 'India')

print(f"player :{player}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'hyd', 'mum', 'kol', 'del']
print(f"cities :{cities}")

res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 23)
print(f"res2 :{res2}")

print("pop".center(40, "-"))
emp = {'empid': 101, 'ename': "Slater", 'dob': "15/10/1988", 'desig': 'MGR', 'dept': 'finance'}
print(f"emp :{emp}")

res = emp.pop('dept')
print(f"res :{res}")
print(f"emp :{emp}")

# res1 =emp.pop()
print("popitem".center(40,"-"))
emp = {'empid': 101, 'ename': "Slater", 'dob': "15/10/1988", 'desig': 'MGR', 'dept': 'finance'}
print(f"emp :{emp}")

res = emp.popitem()
print(f"res :{res}")
print(F"emp :{emp}")

res = emp.popitem()
print(f"res :{res}")
print(F"emp :{emp}")


