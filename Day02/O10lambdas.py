
def add(x, y):
    return x + y

a = add

res = a(10, 20)
print(f"res :{res}")

print("-" * 40)

b = lambda i, j: i + j
res = b(35, 45)
print(f"res :{res}")

# lambdas are best used with three other functions
"""
1. map      2. filter    3. reduce(functools)

"""
# map
l = list(range(1, 11))
print(f"l   :{l}")

res = list(map(lambda x: x ** 2, l))
print(f"res :{res}")

print("-" * 40)

from calendar import month_name
print(list(month_name))

for m in list(month_name):
    print(m[0:3].lower(), end=" ")
print()

months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']
print(f"months Before :{months}")
srtdMons = sorted(months, key=list(map(lambda m: m[0:3].lower(), list(month_name))).index)
print(f"sorted months :{srtdMons}")


def monthName(mon):
    l = []
    for m in list(month_name):
        l.append(str(m[0:3].lower()))
    if mon in l:
        return l.index(mon)


srtdMon1 = sorted(months, key=monthName)
print(f"sorted :{srtdMon1}")

# filters
print("-" * 40)
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

# reduce
from functools import reduce
l = [8, 4, 6, 2, 9, 7, 10, 3, 12]
print(f"l :{l}")

res1 = reduce(lambda x, y: x + y, l)
print(f"res1 :{res1}")

print("-" * 40)
res2 = reduce(lambda x, y: x if x > y else y, l)
print(f"res2: {res2}")
