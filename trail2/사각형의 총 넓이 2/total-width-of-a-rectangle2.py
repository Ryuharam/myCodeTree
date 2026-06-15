n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
board = [[False for _ in range(201)] for _ in range(201)]

for i in range(n):
    for r in range(x1[i], x2[i]):
        for c in range(y1[i], y2[i]):
            board[r][c] = True


sum = 0
for r in board:
    for c in r:
        if c:
            sum += 1

print(sum)