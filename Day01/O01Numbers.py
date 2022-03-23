
"""
1. int
2. float
3. complex numbers

4.boolean

"""

a = 10
b = -10
print(f"a :{a}")
print(type(a))                  # rtti - runtime type identification
print(f"b :{b}")
print(type(b))

print("-" * 40)
c = 15.8
d = -15.8
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 40)
e = 2e3
f = -2e3
print(f"e :{e}")
print(type(e))
print(f"f :{f}")
print(type(f))

print("-" * 40)
g =  4 + 5j
h =  4 - 5j
print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("conversion".center(40, "-"))
a = -150
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o111)        # octal
print(0o15)         # octal
print(0xe)          # hexa
print(0xa)          # hexa

b = 12.895
print(f"b :{b}")
print(type(b))
print(f"{type(int(b))}\t\t{int(b)}")

print('Number system conversion'.center(50, "-"))
a = 100
print(f"a :{a}")
print(f"oct :{oct(a)}")
print(f"bin :{bin(a)}")
print(f"hex :{hex(a)}")

