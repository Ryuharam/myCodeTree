n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]

s = 1

for c in range(n):
    for r in range(n):
        arr[r][c] = s
        s += 1

for row in arr:
    for col in row:
        print(col, end=" ")
    print()