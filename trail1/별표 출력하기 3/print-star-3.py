n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ",end=" ")
    for _ in range(2 * n - 1 -2*i):
        print("*",end=" ")
    print()