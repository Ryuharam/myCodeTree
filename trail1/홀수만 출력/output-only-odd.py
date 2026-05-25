a, b = input().split()

a = int(a)
b = int(b)

a = a if a%2==1 else a+1

for i in range(a, b+1,2):
    print(i, end=" ")