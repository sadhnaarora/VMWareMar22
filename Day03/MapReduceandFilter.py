

def square(n):
    return n ** 2

l = list(range(1, 11))

res = list(map(square, l))
print(f"res :{res}")

res1 = list(map(lambda x : x ** 2, l))
print(f"res1 :{res1}")
