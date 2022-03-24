import dataclasses

s1 = set()
print(F"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = set(range(1, 6))
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = {1, 2, 3, 4.6, 5.9, 6.3, 'seven', 'eight', 'nine', True, False, 10 + 1j, 9 + 2j}
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s4 = {1, 2, 3}
print(f"s4 :{s4}")
s4.add(4)
s4.add(1)
s4.add(2)
s4.add(5)
s4.add(2)
s4.add(3)
print(f"s4 :{s4}")

print('update'.center(40, "-"))
s4.update([1, 4, 1])
s4.update([3, 2, 5])
s4.update([5, 6, 7])
s4.update([3, 8, 9])
print(f"s4 :{s4}")

print("pop".center(40, "-"))
res = s4.pop()
print(f"res :{res}")
print(f"s4 :{s4}")

print("remove".center(40, "-"))
s4.remove(5)
print(f"s4 :{s4}")

# s4.remove(1)

print("discard".center(40,"-"))
s4.discard(7)
print(f"s4 :{s4}")

s4.discard(1)
print("-" * 40)

A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
print("A union B :", A | B)
print("B union A :", B.union(A))

print("-" * 40)
print("A intersection B :", A & B)
print("B intersection A :", B.intersection(A))

print("-" * 40)
print("A difference B :", A - B)
print("B difference A :", B.difference(A))

print("-" * 40)
print("A symmetric difference B :", A ^ B)
print("B symmetric difference A :", B.symmetric_difference(A))

# frozen set - immutable
s = frozenset([1, 2, 3, 4, 5])
print(f"s :{s}")


# functions -> decorators
