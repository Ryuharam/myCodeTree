import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

possible = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

dr = [1, 0]
dc = [0, 1]
answer = 0

def dfs(r:int, c:int):
    global answer

    if r == N-1 and c == M-1:
        answer = 1
        return

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr and nr < N and 0 <= nc and nc < M and not visited[nr][nc] and possible[nr][nc] == 1:
            visited[nr][nc] = True
            dfs(nr, nc)

visited[0][0] = True
dfs(0,0)
print(answer)