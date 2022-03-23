"""
print(data, sep="", end="\n")

1. continue     - skip the iteration
2. break        - stop the iteration
3. else         - executed after the for loop
"""

for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for j in range(1, 25):
    # if j >= 20:
    #     break
    if j % 3 == 0:
        print(j, end=" ")
    else:
        continue
else:
    print("\nfor loop executed successfully....")
