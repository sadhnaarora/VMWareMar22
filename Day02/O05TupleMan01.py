
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)
t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)
t3 = tuple(range(10, 101, 10))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3, 4
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t6 = tuple(range(1, 6))
print(f"t6 :{t6}")
# t6[2] = "three"

l = list(t6)
print(f"l :{l}")
l.extend([6, 7, 8, 9])
print(f"l :{l}")
t = tuple(l)
print(f"t :{t}")
print(t[0])
print(t[0:5])
print(t[-1])
print(t[-1:-4:-1])

print("-" * 40)
print(dir(t))
print('count'.center(4, "-"))
t =(1, 2, 1, 2, 1, 1, 3, 1, 2, 1, 3, 1, 4, 1, 2, 1, 1, 3)
print(f"t :{t}")
print(t.count(1))

print("index".center(40, "-"))
t =(1, 2, 1, 2, 1, 1, 3, 1, 2, 1, 3, 1, 4, 1, 2, 1, 1, 3)
print(f"t :{t}")
print(t.index(3))
print(t.index(3, 7))
print(t.index(3, 11))

