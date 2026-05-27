n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ",end=" ")
    for _ in range(2*n - 1 - 2*i):
        print("*",end=" ")
    print()

for i in range(n-1):
    for _ in range(n-2-i):
        print(" ",end=" ")
    for _ in range(3+2*i):
        print("*",end=" ")
    print()