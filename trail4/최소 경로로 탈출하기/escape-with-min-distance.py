import sys
from collections import deque

input = sys.stdin.readline

N, M = list(map(int, input().split()))

possible = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
step = [[0 for _ in range(M)] for _ in range(N)]

dq = deque()

visited[0][0] = True
dq.append((0,0))

def canMove(r, c):
    return 0 <= r and r < N and 0 <= c and c < M and not visited[r][c] and possible[r][c] == 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while dq:
    r, c = dq.popleft()

    if r == N-1 and c == M-1:
        break

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if canMove(nr, nc):
            visited[nr][nc] = True
            step[nr][nc] = step[r][c] + 1
            dq.append((nr, nc))

if step[N-1][M-1] == 0:
    print(-1)
else:
    print(step[N-1][M-1])
