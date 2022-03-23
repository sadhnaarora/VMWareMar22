
print("pop".center(40, "-"))
l = [1, 2, 3, 1, 2, 2, 1, 3, 1, 2, 1, 1, 3, 4, 1, 2, 1]
print(f"l :{l}")
res = l.pop(0)
print(f"res :{res}")
print(f"l :{l}")
print(len(l))
# l.pop(16)

res = l.pop()           # removes the last element
print(f"res :{res}")
print(f"l :{l}")

print("remove".center(40, "-"))
l = [1, 2, 3, 1, 2, 2, 1, 3, 1, 2, 1, 1, 3, 4, 1, 2, 1]
print(f"l :{l}")

res = l.remove(1)
print(f"res :{res}")
print(f"l :{l}")

while True:
    try:
        l.remove(1)
    except ValueError:
        break

print(f"l :{l}")

print("sort".center(40, "-"))
l = [10, 7, 9, 2, 8, 1, 4, 6, 3, 5]
print(f"l :{l}")

"""
sort = will sort the original list
sorted = will return a copy of the sorted list, original list will remain the same
"""

res1 = sorted(l)
print(f"res1 :{res1}")

res2 = sorted(l, reverse=True)
print(f"res2 :{res2}")

print("-" * 40)
l = [10, 'zebra', 'apple', 7, 'yellow', 'blue', 9, 'violet', 'cat',  2, 'queen', 'dog', 8,
     1, 'pink', 'maroon', 4, 'green', 'red',  6, 3, 5, 19, 1025, 112, 28, 2903, 215]
print(f"l :{l}")

print("-" * 40)
res = sorted(l, key=ascii)

print(f"res :{res}")

"""
cities = ['vishakapatnam', 'bangalore', 'pune', 'mysore', 'delhi', 'thiruvananthapuram',
          'hyderabad', 'kanyakumari', 'ooty', 'madurai', 'mumbai']
          
months = ['dec', 'oct', 'jun', 'jul', 'jan', 'apr', 'feb', 'nov', 'may', 'aug', 'sep', 'mar']


sort cities based on the length of names
sort months based on calendar

"""