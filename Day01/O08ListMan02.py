
"""
'append', 'clear', 'copy', 'count', 'extend', 'index',
'insert', 'pop', 'remove', 'reverse', 'sort'
"""
# add - append, extend, insert

print("append".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.append(6)
l1.append("seven")
l1.append("eight")
l1.append([9, 10, 11, 12])
print(f"l1 :{l1}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = [6, 7, 8, 9, 10]
print(f"l2: {l2}")
l2.extend([11, 12, 13, 14, 15])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l3 = list(range(1, 6))
print(f"l3 :{l3}")
l3.insert(1, 1.5)
l3.insert(3, 2.5)
l3.insert(5, 3.5)
l3.insert(7, 4.5)
print(f"l3 :{l3}")

print("count".center(40, "-"))
l = [1, 2, 1, 2, 2, 1, 3, 1, 2, 1, 1, 3, 4, 1, 2, 1]
print(f"l :{l}")
print("1 :", l.count(1))
print("2 :", l.count(2))


print("index".center(40, "-"))
l = [1, 2, 3, 1, 2, 2, 1, 3, 1, 2, 1, 1, 3, 4, 1, 2, 1]
print(f"l :{l}")
print(l.index(3))
print(l.index(3, 4))
print(l.index(3, 8))
# print(l.index(3, 13))

print("copy".center(40, "-"))
l1 = [1,2,3,4,5]
print(f"l1 Before :{l1}")
l2 = l1             # shallow copy  ->      share the adress and values
print(f"l2 Before :{l2}")

print("-" * 40)
l2.extend([6, 7, 8])
print(f"l2 :{l2}")
print(f"l1 :{l1}")

print("-" * 40)
l3 = list(range(2, 11, 2))
print(f"l3 Before :{l3}")
l4 = l3.copy()          #Deep copy - copy only the values
print(f"l4 Before :{l4}")

print("-" * 40)
l4.extend([12, 14, 16])
print(f"l4 After :{l4}")
print(f"l3 After :{l3}")

print("-" * 40)
l5 = [10, 20, 30, 40, [5, 15, 25, 35, 45], 50]
print(f"l5 Before :{l5}")
l6 = l5.copy()
print(f"l6 Before :{l6}")

print("-" * 40)
l6[4].extend([55, 65, 75])
print(f"l6 After :{l6}")
print(f"l5 After :{l5}")

print("-" * 40)
from copy import deepcopy
l7 = [10, 20, 30, 40, ['a', 'b', 'c'], 50]
print(f"l7 Before :{l7}")
l8 = deepcopy(l7)
print(f"l8 :{l8}")

print("-" * 40)
l8[4].extend(['d', 'e', 'f'])
print(f"l8 After :{l8}")
print(f"l7 After :{l7}")
