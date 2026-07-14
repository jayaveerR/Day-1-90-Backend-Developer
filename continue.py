"""
for i in range(1,6):
    if i == 3:
        print("aboo")
        continue
    print(i)


for row in range(3):
    for col in range(3):
        print(" * ", end="")
    print()


for row in range(1,6):
    for col in range(1 , row + 1):
        print(col , end="")
    print()


for row in range(1,6):
    for col in range("*", row + 1):
        print("*" , end="")
    print()
"""

for row in range(1 , 6):
    for col in range(1, row + 2):
        print(" A ", end="")
    print()