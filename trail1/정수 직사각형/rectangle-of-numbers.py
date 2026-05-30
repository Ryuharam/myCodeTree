n, m = list(map(int, input().split()))

arr = [[0 for _ in range(m)] for _ in range(n)]

s = 1

for i in range(n):
    for j in range(m):
        arr[i][j] = s
        s += 1

for r in arr:
    for c in r:
        print(c, end=" ")
    print("")  