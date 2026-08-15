import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]
ans = [[0 for _ in range(N)] for _ in range(N)]

dq = deque()

for r in range(N):
    for c in range(N):
        if arr[r][c] == 2:
            ans[r][c] = 0
            dq.append((r, c, 0))
        elif arr[r][c] == 0:
            ans[r][c] = -1
        elif arr[r][c] == 1:
            ans[r][c] = -2

def is_possible(r, c):
    return 0 <= r and r < N and 0 <= c and c < N and arr[r][c] == 1 and ans[r][c] == -2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while dq:
    r, c, t = dq.popleft()

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if is_possible(nr, nc):
            ans[nr][nc] = t+1
            dq.append((nr, nc, t+1))

for a in ans:
    print(*a)