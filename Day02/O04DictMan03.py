

print("items".center(40, "-"))
emp = {
    'emp1' :{'empid': 123, 'ename': 'Jack', 'age': 29, 'dept': 'MKT', 'sal': 65000},
    'emp2' :{'empid': 298, 'ename': 'Jill', 'age': 32, 'dept': 'Fin', 'sal': 85000},
    'emp3' :{'empid': 305, 'ename': 'Peter', 'age': 37, 'dept': 'HR', 'sal': 145000}
}

print(f"emp :{emp}")
print("-" * 40)

print(f"emp1 :{emp['emp1']}")
print("-" * 40)

print(f"emp2 :{emp['emp2']}")
print("-" * 40)

print(f"emp3 :{emp['emp3']}")
print("-" * 40)

# items = keys() + values()
for ky, info in emp.items():
    print(ky)
    print("------")
    for k, v in info.items():
        print(k, '=>', v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'empid': 123, 'ename': 'Jack', 'age': 29, 'dept': 'MKT', 'sal': 65000}
emp2 = {'empid': 298, 'ename': 'Jill', 'age': 32, 'desig': "PL", 'sal': 85000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("-" * 40)
d1 = {1: 2, 2: 4}
d2 = {3: 9, 4: 16}
d3 = {5: 25, 6 :36}

print(d1, d2, d3)

d4 = {**d1, **d2, **d3}
print(f"d4 :{d4}")

l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
print(*l1)

keys = ['sachin', 'messi', 'fedrer', 'sindhu', 'pillai', 'tyson']
values = ['cricket', 'soccer', 'tennis', 'badmiton', 'hockey', 'boxing']
d1 = dict(zip(keys, values))
print(f"d1 :{d1}")
