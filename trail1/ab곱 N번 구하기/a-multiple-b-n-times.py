n = int(input())

for _ in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)

    sum = 1
    for i in range(a, b+1):
        sum *= i
    print(sum)