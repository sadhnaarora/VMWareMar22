
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4, 5]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4.5, 5.8, 6.2, 'seven', 'eight', 'nine', True, False, 12+2j, 13+9j]
print(f"l4: {l4}")
print(type(l4))
print(f"l4[3] :{l4[3]}")

print("-" * 40)
l4[4] = 58
del l4[10]
print(f"l4 :{l4}")
print(f"l4[-1] :{l4[-1]}")
print(f"len(l4) :{len(l4)}")
# l4[13] = "hello"
print(f"l4 :{l4}")


print("-" * 40)
print(dir(l4))
