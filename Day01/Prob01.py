
for i in range(6, 1, -1):
    for j in range(7-i, 1, -1):
        print(" ", end="")
    for k in range(1, i):
        print(k, end=" ")
    print()

for i in range(2, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

