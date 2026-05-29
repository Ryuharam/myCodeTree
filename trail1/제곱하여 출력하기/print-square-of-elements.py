n = int(input())

num = list(map(int, input().split()))

res = [i**2 for i in num ]

for r in res:
    print(r,end=" ")