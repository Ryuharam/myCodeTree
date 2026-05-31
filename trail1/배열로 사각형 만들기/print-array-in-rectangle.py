arr = [[1 for _ in range(5)] for _ in range(5)]

for r in range(1, 5):
    for c in range(1, 5):
        arr[r][c] = arr[r-1][c] + arr[r][c-1]

for row in arr:
    for col in row:
        print(col, end=" ")
    print()