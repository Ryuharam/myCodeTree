import sys
from collections import deque

input = sys.stdin.readline

N, K, U, D = list(map(int, input().split()))

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_cnt = 0

def is_possible(r: int, c: int):
    return 0 <= r and r < N and 0 <= c and c < N and not visited[r][c] 

def bfs(r: int, c: int) -> int:
    if visited[r][c]:
        return 0

    visited[r][c] = True
    dq = deque()
    dq.append((r,c))
    cnt = 0

    while dq:
        cr, cc = dq.popleft()
        cnt += 1

        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]

            if is_possible(nr, nc):
                diff = abs(board[cr][cc] - board[nr][nc])
                if U <= diff and diff <= D:
                    visited[nr][nc] = True
                    dq.append((nr, nc))
    return cnt

max_cnt = []
for r in range(N):
    for c in range(N):
        max_cnt.append(bfs(r, c))

sorted_cnt = sorted(max_cnt, key=lambda x: -x)

ans = 0
for k in range(K):  
    ans += sorted_cnt[k]

print(ans)  