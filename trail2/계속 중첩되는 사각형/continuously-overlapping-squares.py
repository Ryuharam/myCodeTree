n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a + 100)
    y1.append(b + 100)
    x2.append(c + 100)
    y2.append(d + 100)

# Please write your code here.

board = [[0]*201 for _ in range(201)]

for i in range(n):
    for r in range(x1[i], x2[i]):
        for c in range(y1[i], y2[i]):
            board[r][c] = 1 if i%2==0 else 2

cnt = 0

for r in board:
    for c in r:
        if c == 2:
            cnt += 1

print(cnt)
