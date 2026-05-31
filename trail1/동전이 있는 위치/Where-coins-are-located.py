n, m = tuple(map(int, input().split()))

arr = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    r,c = tuple(map(int, input().split()))
    arr[r][c] = 1

for row in arr[1:]:
    for col in row[1:]:
        print(col, end=" ")
    print()